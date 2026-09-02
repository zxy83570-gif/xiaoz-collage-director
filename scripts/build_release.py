#!/usr/bin/env python3
"""Build a deterministic, preflight-gated release archive."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import subprocess
import sys
import tarfile
from pathlib import Path


EXCLUDED_PARTS = {"__pycache__", ".git", "dist"}
EXCLUDED_NAMES = {".DS_Store"}


def release_files(root: Path) -> list[Path]:
    result: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        if path.name in EXCLUDED_NAMES or path.suffix == ".pyc":
            continue
        result.append(path)
    return sorted(result, key=lambda item: item.relative_to(root).as_posix())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    root = args.root.resolve()
    preflight = root / "scripts/preflight.py"
    completed = subprocess.run([sys.executable, str(preflight), str(root)], check=False)
    if completed.returncode:
        return completed.returncode

    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    archive_name = f"{root.name}-{version}.tar.gz"
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / archive_name

    with archive.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as compressed:
            with tarfile.open(fileobj=compressed, mode="w") as bundle:
                for path in release_files(root):
                    relative = path.relative_to(root)
                    info = bundle.gettarinfo(str(path), arcname=f"{root.name}/{relative.as_posix()}")
                    info.uid = 0
                    info.gid = 0
                    info.uname = ""
                    info.gname = ""
                    info.mtime = 0
                    with path.open("rb") as source:
                        bundle.addfile(info, source)

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(archive.suffix + ".sha256")
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(f"OK: {archive}")
    print(f"SHA256: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

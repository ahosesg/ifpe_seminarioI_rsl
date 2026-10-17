"""Compara os arquivos recebidos com a fotografia original do export Prism."""

import hashlib
import json
import os
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    # Os títulos de alguns PDFs excedem o limite clássico de caminhos do Windows.
    if os.name == "nt" and not str(root).startswith("\\\\?\\"):
        root = Path("\\\\?\\" + str(root))
    manifest = json.loads(
        (root / "docs/importacao_prism/manifesto.json").read_text(encoding="utf-8")
    )
    failures = []
    for entry in manifest["files"]:
        relative = Path(entry["path"])
        target = root / relative
        if relative.is_absolute() or not target.resolve().is_relative_to(root.resolve()):
            failures.append(f"Caminho invalido: {entry['path']}")
            continue
        if not target.is_file():
            failures.append(f"Ausente: {entry['path']}")
            continue
        with target.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        if target.stat().st_size != entry["size"] or digest != entry["sha256"]:
            failures.append(f"Alterado: {entry['path']}")
    count = len(manifest["files"])
    if count != manifest["file_count"]:
        failures.append("A contagem do manifesto e inconsistente.")
    if sum(entry["size"] for entry in manifest["files"]) != manifest["total_bytes"]:
        failures.append("O total de bytes do manifesto e inconsistente.")
    if failures:
        print("\n".join(failures))
        print(f"{len(failures)} divergencia(s) em relacao a importacao original.")
        return 1
    print(f"OK: {count} arquivos recebidos conferem com a importacao original.")
    print(f"Total: {manifest['total_bytes']} bytes. SHA-256 de todos os arquivos confere.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from pathlib import Path
import os

from pypdf import PdfReader, PdfWriter

for path in (Path("static/MY_CV.pdf"), Path("public/MY_CV.pdf")):
    reader = PdfReader(str(path))
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    metadata = dict(reader.metadata or {})
    metadata["/Title"] = "Aritrabha Majumdar's CV"
    writer.add_metadata(metadata)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    with temporary_path.open("wb") as output:
        writer.write(output)
    os.replace(temporary_path, path)

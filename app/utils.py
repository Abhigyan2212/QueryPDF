import os
from fastapi import UploadFile
from pathlib import Path

def save_pdf(file: UploadFile, destination: str) -> str:
    destination_path = Path(destination) / file.filename
    with open(destination_path, "wb") as buffer:
        buffer.write(file.file.read())
    return str(destination_path)

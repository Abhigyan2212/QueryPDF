from fastapi import FastAPI, UploadFile, File, WebSocket, WebSocketDisconnect, Depends
from app.database import SessionLocal
from app.models import Document
from app.schemas import DocumentCreate, DocumentResponse
from app.utils import save_pdf
from app.nlp import extract_text_from_pdf
from sqlalchemy.orm import Session
import os

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = save_pdf(file, "pdf_uploads")
    text_content = extract_text_from_pdf(file_path)

    document = Document(filename=file.filename, content=text_content)
    db.add(document)
    db.commit()
    db.refresh(document)

    return DocumentResponse(id=document.id, filename=document.filename, upload_date=document.upload_date)

@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            question = await websocket.receive_text()
            answer = "Processed answer based on question: " + question
            await websocket.send_text(answer)
    except WebSocketDisconnect:
        print("Client disconnected")

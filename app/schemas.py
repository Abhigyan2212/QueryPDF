from pydantic import BaseModel
from datetime import datetime

class DocumentCreate(BaseModel):
    filename: str
    content: str

class DocumentResponse(DocumentCreate):
    id: int
    upload_date: datetime

    class Config:
        orm_mode = True

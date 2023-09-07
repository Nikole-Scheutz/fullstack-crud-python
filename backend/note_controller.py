from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import MetaData

from .service import note_service

from .repository import models, schemas
from .repository.database import engine, SessionLocal
models.Base.metadata.create_all(bind=engine) 


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.get("/api/notes/{note_id}", response_model=schemas.Note)
def get_note(note_id: int, db = Depends(get_db)):
    note = note_service.get_note(note_id, db)
    return note

@app.get("/api/notes/user/{user_id}")
def get_notes(user_id: int, db = Depends(get_db)):
    notes = note_service.get_notes(user_id, db)
    return notes

@app.post("/api/notes/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db = Depends(get_db)):
    return note_service.create_note(note, db)

@app.put("/api/notes/{note_id}", response_model=schemas.Note)
def edit_note(note_id: int, note: schemas.Note, db: Session = Depends(get_db)):
    return note_service.edit_note(note_id, note, db)

@app.delete("/api/notes/{note_id}")
def delete_note(note_id: int, db = Depends(get_db)):
    note_service.delete_note(note_id, db)


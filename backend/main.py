from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import MetaData

from .repository import note_repository

from .repository import models, schemas
from .repository.database import engine, SessionLocal
from .repository import note_repository


# THIS SHOWS AN ERROR, BUT SEEMS TO WORK ANYWAYS
models.Base.metadata.create_all(bind=engine) 

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/notes/{note_id}", response_model=schemas.Note)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = note_repository.get_note(db, note_id)
    return note

@app.get("/notes/user/{user_id}", response_model=list[schemas.Note])
def get_notes(user_id: int, db: Session = Depends(get_db)):
    notes = note_repository.get_notes(db, user_id)
    return notes

@app.post("/notes/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return note_repository.create_note(db, note)

@app.put("/api/notes/{note_id}", response_model=schemas.Note)
def edit_note(note_id: int, note: schemas.Note, db: Session = Depends(get_db)):
    return note_repository.edit_note(db, note_id, note)

@app.delete("/api/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note_repository.delete_note(db, note_id)


from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import MetaData

from .repository import repository, models, schemas
from .repository.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) # THIS SHOWS AN ERROR, BUT SEEMS TO WORK ANYWAYS

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/note/{note_id}", response_model=schemas.Note)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = repository.get_note(db, note_id)
    return note

@app.post("/note/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return repository.create_note(db, note)

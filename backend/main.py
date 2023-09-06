from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import MetaData

from . import repository, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) # THIS SHOWS AN ERROR, BUT SEEMS TO WORK ANYWAYS

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/note", response_model=schemas.Note)
def get_note(db: Session = Depends(get_db)):
    note = repository.get_note(db, 1)
    return note

@app.post("/note/{user_id}", response_model=schemas.Note)
def create_note(user_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    note.user_id = user_id
    return repository.create_note(db, note)

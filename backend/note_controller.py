from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

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
def get_note(note_id: int, response: Response, db = Depends(get_db)):
    try:
        note = note_service.get_note(note_id, db)
        response.status_code = status.HTTP_200_OK
        return note

    except Exception as error:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(error))


@app.get("/api/notes/user/{user_id}")
def get_notes(user_id: int, response: Response, db = Depends(get_db)):
    try:
        notes = note_service.get_notes(user_id, db)
        response.status_code = status.HTTP_200_OK
        return notes

    except Exception as error:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(error))


@app.post("/api/notes/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, response: Response, db = Depends(get_db)):
    try:
        new_note = note_service.create_note(note, db)
        response.status_code = status.HTTP_201_CREATED
        return new_note

    except Exception as error:
        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY, detail = str(error))


@app.put("/api/notes/{note_id}", response_model=schemas.Note)
def edit_note(note_id: int, note: schemas.Note, response: Response, db: Session = Depends(get_db)):
    try:
        edited_note = note_service.edit_note(note_id, note, db)
        response.status_code = status.HTTP_200_OK
        return edited_note

    except Exception as error:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(error))


@app.delete("/api/notes/{note_id}")
def delete_note(note_id: int, response: Response, db = Depends(get_db)):
    try:
        note_service.delete_note(note_id, db)
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    except Exception as error:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(error))


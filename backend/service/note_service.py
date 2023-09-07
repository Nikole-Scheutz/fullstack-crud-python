from ..repository import note_repository

from ..repository import models, schemas
from ..repository import note_repository
from sqlalchemy.orm import Session


def get_note(note_id: int, db: Session) -> schemas.Note:
    note = note_repository.get_note(db, note_id)
    return note

def get_notes(user_id: int, db: Session) -> list[models.Note]:
    return note_repository.get_notes(db, user_id)

def create_note(note: schemas.NoteCreate, db: Session) -> schemas.Note:
    new_note = note_repository.create_note(db, note)
    return new_note

def edit_note(note_id: int, new_note: schemas.Note, db: Session) -> schemas.Note:
    edited_note = note_repository.edit_note(db, note_id, new_note)
    return edited_note

def delete_note(note_id: int, db: Session):
    note_repository.delete_note(db, note_id)


from sqlalchemy.orm import Session

from . import models, schemas


def create_note(db: Session, note: schemas.NoteCreate):


    db_item = models.Note(**note.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.note_id == note_id).first()

def get_notes(db: Session, user_id: int):
    return 0

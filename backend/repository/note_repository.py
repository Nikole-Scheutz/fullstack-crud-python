from sqlalchemy.orm import Session

from . import models, schemas

def create_note(db: Session, note: schemas.NoteCreate):
    db_item = models.Note(**note.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_note(db: Session, note_id: int) -> schemas.Note | Exception:
    try:
        return db.query(models.Note).filter(models.Note.note_id == note_id).one()
    except Exception as error:
        raise Exception(type(error).__name__)

def get_notes(db: Session, user_id: int) -> list[models.Note]:
    assert db.query(models.Note) is not None
    return db.query(models.Note).filter(models.Note.user_id == user_id).all()

def edit_note(db: Session, note_id: int, note: schemas.Note):
    db.query(models.Note)\
            .filter(models.Note.note_id == note_id)\
            .update({
                "title": note.title,
                "content": note.content,
                "user_id": note.user_id,
                },
                synchronize_session="evaluate"
                )
    db.commit()
    return db.query(models.Note).filter(models.Note.note_id == note_id).first()
    
def delete_note(db: Session, note_id: int):
    note = get_note(db, note_id)
    if type(note) == None:
        return False
    db.delete(note)
    return db.commit()


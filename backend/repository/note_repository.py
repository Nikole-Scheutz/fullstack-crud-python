from sqlalchemy.orm import Session

from . import models, schemas


def create_note(db: Session, note: schemas.NoteCreate):
    try:
        db_item = models.Note(**note.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    except Exception as error:
        error_string = f"Create error: {error}"
        raise Exception(error_string)


def get_note(db: Session, note_id: int) -> schemas.Note | Exception:
    try:
        return db.query(models.Note).filter(models.Note.note_id == note_id).one()
    
    except:
        error_string = f"Note with note_id={note_id} does not exist"
        raise Exception(error_string)


def get_notes(db: Session, user_id: int) -> list[models.Note]:
    try:
        return db.query(models.Note).filter(models.Note.user_id == user_id).all()
    
    except Exception as error:
        raise Exception(type(error).__name__)


def edit_note(db: Session, note_id: int, note: schemas.Note):
    try:
        get_note(db, note_id) # This is required to cause the except clause to run
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
    
    except Exception as error:
        error_string = f"Edit error: {error}"
        raise Exception(error_string)


def delete_note(db: Session, note_id: int):
    try:
        note = get_note(db, note_id)
        if type(note) == None:
            return False
        db.delete(note)
        return db.commit()
    
    except Exception as error:
        error_string = f"Delete error: {error}"
        raise Exception(error_string)


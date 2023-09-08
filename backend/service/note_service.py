from sqlalchemy.orm import Session

from ..repository import note_repository, models, schemas


def get_note(note_id: int, db: Session) -> schemas.Note | Exception:
    try:
        note = note_repository.get_note(db, note_id)
        return note
    
    except Exception as error:
        raise error


def get_notes(user_id: int, db: Session) -> list[models.Note]:
    try:
        return note_repository.get_notes(db, user_id)

    except Exception as error:
        raise error


def create_note(note: schemas.NoteCreate, db: Session) -> schemas.Note:
    try:
        new_note = note_repository.create_note(db, note)
        return new_note

    except Exception as error:
        raise error


def edit_note(note_id: int, new_note: schemas.Note, db: Session) -> schemas.Note:
    try:
        edited_note = note_repository.edit_note(db, note_id, new_note)
        return edited_note

    except Exception as error:
        print(str(error))
        raise error


def delete_note(note_id: int, db: Session):
    try:
        note_repository.delete_note(db, note_id)

    except Exception as error:
        raise error


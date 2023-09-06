from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Integer, String, Column, ForeignKey

SQLALCHEMY_DATABASE_URL = 'sqlite:///mydb.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id =  Column(Integer, primary_key=True, auto_increment=True, unique=True)
    username = Column(String, unique=True)
    password = Column(String)

    notes = relationship("Note", back_populates="owner")

    def __init__(self, username, password):
        self = User(username, password)

class Note(Base):
    __tablename__ = "notes"
    note_id = Column(Integer, primary_key=True, auto_increment=True, unique=True)
    title = Column(String, unique=True)
    content = Column(String)

    user_id = Column(Integer, ForeignKey("users.user_id"))
    owner = relationship("User", back_populates="notes")

    def __init__(self, user_id, title, contents):
        self = Note(user_id, title, contents)

class UserRepo(SQLRepo):
    def __init__(self):
        SQLRepo(model_orm=User, engine=engine)

class NoteRepo(SQLRepo):
    def __init__(self):
        self = SQLRepo(model_orm=Note, engine=engine, table="notes")

    def create_note(self, user_id, title, contents):
        self.add(Note(user_id, title, contents))

    def get_note(self, note_id):
        return self.filter_by(note_id = note_id)

    #def edit_note(self, input = {"note_id": Integer, "title": String, "contents": String}):
    #    current_note = self.get_note(input["note_id"])
    #    current_note.update(title = input["title"])

noterepo = NoteRepo()

noterepo.create_note(1, "TITLE", "CONTENTS")


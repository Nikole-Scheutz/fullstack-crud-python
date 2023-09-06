from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    user_id =  Column(Integer, primary_key=True, auto_increment=True, unique=True)
    username = Column(String, unique=True)
    password = Column(String)

    notes = relationship("Note", back_populates="owner")

#    def __init__(self, username, password):
#        self = User(username, password)

class Note(Base):
    __tablename__ = "notes"
    note_id = Column(Integer, primary_key=True, auto_increment=True, unique=True)
    title = Column(String, unique=True)
    content = Column(String)

    user_id = Column(Integer, ForeignKey("users.user_id"))
    owner = relationship("User", back_populates="notes")

#    def __init__(self, user_id, title, contents):
#        self = Note(user_id, title, contents)

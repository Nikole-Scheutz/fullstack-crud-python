from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from . database import Base

class User(Base):
    __tablename__ = "users"
    user_id =  Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String)

    notes = relationship("Note", back_populates="owner")

class Note(Base):
    __tablename__ = "notes"
    note_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    owner = relationship("User", back_populates="notes")


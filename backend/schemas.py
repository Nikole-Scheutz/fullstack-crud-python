from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    user_id: int

class Note(NoteBase):
    note_id: int
    user_id: int
    title: str
    content: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    notes: list[Note] = []
    
    class Config:
        orm_mode = True

from fastapi import FastAPI
from pydantic import BaseModel
from flask import request

app = FastAPI()

# Controller
@app.route('/api/notes', methods=["GET", "POST"])
def controller_notes():
    request_data = request.get_data()
    if request.method == "GET":
        return service_get_notes(request_data)
    elif request.method == "POST":
        return service_create_note(request_data)

@app.route('/api/notes/:<id>', methods=["GET", "PUT", "DELETE"])
def controller_specific_note(id):
    request_data = request.get_data()
    if request.method == "GET":
        return service_get_note(request_data)
    elif request.method == "PUT":
        return service_edit_note(request_data)
    elif request.method == "DELETE":
        return service_delete_note(request_data)

@app.route('/api/auth/:<username>', methods=["GET", "POST"])
def controller_auth():
    request_data = request.get_data()
    if request.method == "POST":
        return service_login(request_data)
    else:
        return service_login_prompt(request_data)


# Service
# TODO


# Repository
def get_notes(): #get ALL notes
    pass

def get_note(note_id): #get a single note
    pass

def create_note(user_id, title, contents): #create a note for a user
    pass

def edit_note(note_id, contents):
    note = get_note(note_id)
    note["contents"] = contents
    pass

def delete_note(note_id):
    pass

#User specific things
def create_user(username, password):
    pass

def delete_user(user_id):
    user_notes = get_user_notes(user_id)
    for note in user_notes:
        delete_note(note.note_id)
    #then actually delete the user
    pass

def get_user(user_id):
    pass

def get_user_notes(user_id): #get notes USER has access to
    pass


#X Am I done with repo methods? 
#X Do I need more service methods?
#Freaking json-dictionaries
#How to connect service methods with repo methods?
#How will React react?

#!/usr/bin/python3

notes = [];

def create_note(contents, note_list):
    note_list.append(contents);

def read_note(note, note_list):
    try:
        print(note_list[note]);
    except:
        print("ERROR, NOTE NOT IN LIST");

def update_note(note, note_list, contents):
    note_list[note] = contents;

def delete_note(note, note_list):
    note_list.pop(note);

create_note("Hello", notes);
read_note(0, notes);

delete_note(0, notes);
read_note(0, notes);

create_note("Hello", notes);
read_note(0, notes);

update_note(0, notes, "HELLO");
read_note(0, notes);

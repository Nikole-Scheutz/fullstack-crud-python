#!/usr/bin/python3

class Noter:
    def __init__(self):
        self.notes_list = []

    note_list = []

    def create_note(self, contents):
        self.note_list.append(contents);
    
    def read_note(self, note):
        try:
            print(self.note_list[note]);
        except:
            print("ERROR, NOTE NOT IN LIST");
    
    def update_note(self, note, contents):
        self.note_list[note] = contents;
    
    def delete_note(self, note):
        self.note_list.pop(note);

noter = Noter();

noter.create_note("Hello");
noter.read_note(0);

noter.delete_note(0);
noter.read_note(0);

noter.create_note("Hello");
noter.read_note(0);

noter.update_note(0, "HELLO");
noter.read_note(0);

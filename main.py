#!/usr/bin/python3

class Noter:
    def __init__(self):
        self.notes_list = [];

    note_list = [];

    def create(self, contents):
        self.note_list.append(contents);
    
    def read(self, note):
        try:
            print(self.note_list[note]);
        except:
            print("ERROR, NOTE NOT IN LIST");
    
    def update(self, note, contents):
        self.note_list[note] = contents;
    
    def delete(self, note):
        self.note_list.pop(note);

noter = Noter();

noter.create("Hello");
noter.read(0);

noter.delete(0);
noter.read(0);

noter.create("Hello");
noter.read(0);

noter.update(0, "HELLO");
noter.read(0);

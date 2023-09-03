#!/usr/bin/python3

class Noter:
    def __init__(self):
        self.note_list = [];


    def create(self, contents):
        self.note_list.append(contents);
    
    def read(self, note):
        try:
            note = int(note);
            print(self.note_list[note]);
        except:
            print("ERROR, NOTE NOT IN LIST");
    
    def update(self, note, contents):
        note = int(note);
        self.note_list[note] = contents;
    
    def delete(self, note):
        note = int(note);
        self.note_list.pop(note);

    def list(self):
        for i, note in enumerate(self.note_list):
            print("-", i, note);

noter = Noter();

noter.create("Hello");
noter.read(0);

noter.delete(0);
noter.read(0);

noter.create("Hello");
noter.read(0);

noter.update(0, "HELLO");
noter.read(0);

noter.delete(0);

while True:
    user_input = input();
    match user_input:
        case "create":
            note = input("What to save?\n");
            noter.create(note);
            pass;

        case "read":
            note = input("Read which note?\n");
            note = int(note);
            if 0 <= note < len(noter.note_list):
                noter.update(note, "TEST2");
            noter.read(note);
            pass;

        case "update":
            note = input("Edit which note?\n");
            note = int(note);
            if 0 <= note < len(noter.note_list):
                noter.update(note, "TEST2");
            pass;

        case "delete":
            note = input("Delete which note?\n");
            note = int(note);
            if 0 <= note < len(noter.note_list):
                noter.delete(note);
            pass;

        case "list":
            noter.list();

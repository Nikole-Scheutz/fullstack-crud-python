#!/usr/bin/python3
import json

class JSON:
    def __init__(self):
        file = open("data.json");
        data = json.load(file);
        
        for i in data:
            print(i);
        file.close();
        self.data = data;

    def get_note(self, number):
        print(self.data[number]);
        return self.data[number];

    def save_notes(self):
        with open("sample.json", "w") as outfile:
            json.dump(self.data, outfile);

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

jsonner = JSON();
jsonner.get_note("1");
jsonner.save_notes();

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

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
        with open("data.json", "w") as outfile:
            json.dump(self.data, outfile);

class Noter:
    def __init__(self):
        self.note_list = [];
        self.json = JSON();

    def create(self, contents):
        test = {"contents": contents};
        id = int(list(self.json.data.keys())[-1]) + 1;  # set id of note to one more than last
        self.json.data[f"{id}"] = test;

    def read(self, note):
        try:
            print(self.json.data[f"{note}"]["contents"]);
        except:
            print("ERROR, NOTE NOT IN LIST");

    def update(self, note, contents):
        note = int(note);
        self.note_list[note] = contents;

    def delete(self, note):
        self.json.data.pop(f"{note}");

    def list(self):
        for master_key, i in self.json.data.items():
            print("-", master_key, i["contents"]);

noter = Noter();

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
            noter.delete(note);
            pass;

        case "list":
            noter.list();

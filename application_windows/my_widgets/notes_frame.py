import customtkinter
from typing import Any


some_notes_test_data = [f"Notes: {x}" for x in range(1, 11)]

def test_event():
    print("test")


class NotesScrollFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, height=350, width=300, **kwargs)
        
        self.btn_list = []
        for note_index in range(len(some_notes_test_data)):
            current_note = some_notes_test_data[note_index]
            btn = customtkinter.CTkButton(self, text=current_note, command=test_event, width=250)
            btn.grid(row=note_index, padx=25, pady=3)
            self.btn_list.append(btn)
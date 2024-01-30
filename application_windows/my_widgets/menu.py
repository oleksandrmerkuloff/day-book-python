from typing import Any
import customtkinter


class Menu(customtkinter.CTkFrame):
    def __init__(self, master: Any, notes_win, **kwargs):
        super().__init__(master, width=300, height=600, **kwargs)
        self.master = master
        self.notes_win = notes_win
        
        notes_btn = customtkinter.CTkButton(
            self, text="My Notes", command=self.user_notes_event, width=200,
            corner_radius=10
        )
        notes_btn.grid(row=0, column=0, pady=(0, 20))
        
        contact_btn = customtkinter.CTkButton(
            self, text="My Contacts", command=None, width=200,
            corner_radius=10
        )
        contact_btn.grid(row=1, column=0)
    
    def user_notes_event(self):
        self.notes_win(self.master)
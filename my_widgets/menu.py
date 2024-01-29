from typing import Any
import customtkinter


class Menu(customtkinter.CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, width=300, height=600, **kwargs)
        
        contact_btn = customtkinter.CTkButton(
            self, text="My Contacts", command=None, width=200,
            corner_radius=10
        )
        contact_btn.grid(row=0, column=0, pady=(0, 20))
        
        note_btn = customtkinter.CTkButton(
            self, text="My Notes", command=None, width=200,
            corner_radius=10
        )
        note_btn.grid(row=1, column=0)
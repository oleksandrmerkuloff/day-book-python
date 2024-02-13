import customtkinter

from .single_note_window import NoteWindow
from .my_widgets.notes_frame import NotesScrollFrame


class NotesWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #? Window config
        self.geometry("640x480")
        self.resizable(False, False)
        self.title("My Notes")

        #? Widgets
        self.notes = NotesScrollFrame(self)
        self.notes.grid(
            row=0, column=0,
            rowspan=3, columnspan=2,
            padx=(30, 0), pady=(50, 0)
            )

        notes_ordering = customtkinter.CTkOptionMenu(
            self, values=["Order By", "Name", "Created Date", "Deadline"],
            command=self.new_order_by
        )
        notes_ordering.set("Order By")
        notes_ordering.grid(
            row=0, column=2,
            padx=(75, 0), pady=(0, 20),
            sticky="s"
            )

        add_note_btn = customtkinter.CTkButton(self, text="Add Note", command=self.create_new_note)
        add_note_btn.grid(
            row=1, column=2,
            padx=(75, 0), pady=(0, 50),
            sticky="n"
            )

    def create_new_note(self):
        self.new_note_window = NoteWindow(self)

    def new_order_by(self, choice):
        print(choice)

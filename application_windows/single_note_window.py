import customtkinter


class NoteWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #? Window config
        self.geometry("400x300")
        self.resizable(False, False)
        self.title("Program name")
        
        #? Widgets
        self.note_title_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Enter your title:",
            width=200
        )
        self.note_title_entry.place(
            x=15, y=30, relx=0.01, rely=0.01
        )

        self.save_btn = customtkinter.CTkButton(self, text="Save", command=None)
        self.save_btn.place(x=235, y=30, relx=0.01, rely=0.01)

        self.note_body = customtkinter.CTkTextbox(self, height=200, width=360)
        self.note_body.place(
            x=15, y=85, relx=0.01, rely=0.01
        )

import customtkinter

from application_windows.my_widgets import custom_calendar, menu
from application_windows import user_notes, contacts_window


class App(customtkinter.CTk):
    """Class for application here will be include all app windows and widgets"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #? base app settigns
        self.appearance_mode = customtkinter.set_appearance_mode
        self.color_theme = customtkinter.set_default_color_theme("dark-blue")
        self.title("My notebook")
        self.geometry("1280x720")
        self.resizable(False, False)

        #? Widgets
        self.calendar = custom_calendar.CalendarSection(self)
        self.calendar.grid(
            row=0, column=0,
            padx=20, pady=(20, 0),
            )

        self.menu = menu.Menu(self, user_notes.NotesWindow, contacts_window.ContactsWindow)
        self.menu.grid(row=0, column=4, padx=120, pady=(120, 0), sticky="ne")

        # switch appearance_mode
        self.appearance_state = customtkinter.StringVar(value=customtkinter.get_appearance_mode().lower())
        self.current_appearance_mode = customtkinter.CTkSwitch(
            self, text="Light/Dark mode", command=self.switch_appearance_event,
            variable=self.appearance_state, onvalue="light", offvalue="dark",
            height=50, width=100
        )
        self.current_appearance_mode.grid(row=0, column=5, sticky="ne")

    def switch_appearance_event(self):
        self.appearance_mode(
            self.appearance_state.get()
        )

    def run(self) -> None:
        self.mainloop()


if __name__ == "__main__":
    App().run()

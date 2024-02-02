import customtkinter


class PersonalContactWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #? Window config
        self.geometry("400x300")
        self.resizable(False, False)
        self.title("Program name")
        
        #? Widgets

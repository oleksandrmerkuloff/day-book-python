import customtkinter

from .my_widgets.user_contacts import ContactsScrollFrame
from .single_contact_window import PersonalContactWindow


class ContactsWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #? Window config
        self.geometry("640x480")
        self.resizable(False, False)
        self.title("My Contacts")
    
        #? Widgets
        self.contacts_list = ContactsScrollFrame(self)
        self.contacts_list.grid(
            row=0, column=0,
            rowspan=3, columnspan=2,
            padx=(30, 0), pady=(50, 0)
            )

        add_contact_btn = customtkinter.CTkButton(self, text="Add Contact", command=self.add_new_contact)
        add_contact_btn.grid(
            row=0, column=2,
            padx=(75, 0), pady=(0, 70)
            )
    
    def add_new_contact(self):
        PersonalContactWindow(self)

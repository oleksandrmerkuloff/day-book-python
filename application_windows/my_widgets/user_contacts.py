from typing import Any
import customtkinter


friends = "Jenya Vova Bohdan Ilya Vlad Alina".split()


def test_event():
    print("test")


class ContactsScrollFrame(customtkinter.CTkScrollableFrame):
    """ScrollFrame class where user see a contacts list"""
    def __init__(self, master: Any, **kwargs) -> None:
        super().__init__(master,height=350, width=300, **kwargs)
        self.btn_list = []
        for friend in range(len(friends)):
            friend_name = friends[friend]
            btn = customtkinter.CTkButton(self, text=friend_name, command=test_event, width=250)
            btn.grid(row=friend, padx=25, pady=3)
            self.btn_list.append(btn)
            
if __name__ == "__main__":
    print(type(ContactsScrollFrame))
    # test = customtkinter.CTk(friends)
    # test.geometry("1240x720")
    # frame = FriendScrollFrame(test).grid()
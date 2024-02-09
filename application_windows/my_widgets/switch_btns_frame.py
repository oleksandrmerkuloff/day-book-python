from typing import Any
import customtkinter


# def create_switch_btns_frame(self):
#         self.switch_btn_frame = customtkinter.CTkFrame(self, height=50)
#         self.switch_btn_frame.grid(
#             row=8,
#             column=2,
#             columnspan=3,
#             pady=(40, 0)
#             )

class SwitchBtnsFrame(customtkinter.CTkFrame):
    def __init__(self, master: Any, calendar_obj, **kwargs):
        super().__init__(master, **kwargs)
        self.width = 200
        self.height = 50

        prev_month_btn = customtkinter.CTkButton(
            self, text="prev", width=60, command=calendar_obj.decrease_date
        )
        prev_month_btn.grid(row=0, column=0, padx=(0, 50), pady=10)

        next_month_btn = customtkinter.CTkButton(
            self,
            text="next",
            width=60,
            command=calendar_obj.increase_date
            )
        next_month_btn.grid(row=0, column=1, padx=(50, 0), pady=10)

from typing import Any
import customtkinter


class SwitchBtnsFrame(customtkinter.CTkFrame):
    def __init__(self, master: Any, calendar_obj, **kwargs):
        super().__init__(master, **kwargs)
        self.width = 200
        self.height = 50

        self.prev_month_btn = customtkinter.CTkButton(
            self, text="prev", width=60, command=calendar_obj.decrease_date
        )
        self.prev_month_btn.grid(row=0, column=0, padx=(0, 50), pady=10)

        self.today_btn = customtkinter.CTkButton(
            self, text="today",
            width=60,
            command=calendar_obj.to_today
        )
        self.today_btn.grid(row=0, column=1, pady=10)

        self.next_month_btn = customtkinter.CTkButton(
            self,
            text="next",
            width=60,
            command=calendar_obj.increase_date
            )
        self.next_month_btn.grid(row=0, column=2, padx=(50, 0), pady=10)

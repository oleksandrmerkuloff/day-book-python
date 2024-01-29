from typing import Any
import customtkinter
import calendar


class CalendarSection(customtkinter.CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, width=800, height=800, **kwargs)
        
        self.calendar_frame = customtkinter.CTkFrame(self, width=800, height=600)
        self.calendar_frame.grid(row=0, column=0, columnspan=3)
                
        self.switch_btn_frame = customtkinter.CTkFrame(self, height=50)
        self.switch_btn_frame.grid(row=1, column=0, columnspan=3)
        self.prev_month_btn = customtkinter.CTkButton(
            self.switch_btn_frame,
            text="prev",
            width=60
            )
        self.prev_month_btn.grid(row=0, column=0, padx=(0, 50), pady=10)
        self.next_month_btn = customtkinter.CTkButton(
            self.switch_btn_frame,
            text="next",
            width=60
            )
        self.next_month_btn.grid(row=0, column=1, padx=(50, 0), pady=10)


if __name__ == "__main__":
    print(type(CalendarSection))
    test_calendar = calendar.Calendar()
    print(len(test_calendar.monthdatescalendar(2024, 11)))
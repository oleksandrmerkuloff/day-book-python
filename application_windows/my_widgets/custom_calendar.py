import customtkinter
from datetime import date, datetime
import calendar


# class CalendarSection(customtkinter.CTkFrame):
#     def __init__(self, master: Any, **kwargs):
#         super().__init__(master, width=800, height=800, **kwargs)

#         self.calendar_frame = customtkinter.CTkFrame(
#             self,
#             width=800,
#             height=600
#         )
#         self.calendar_frame.grid(row=0, column=0, columnspan=3)

#         self.switch_btn_frame = customtkinter.CTkFrame(self, height=50)
#         self.switch_btn_frame.grid(row=1, column=0, columnspan=3)
#         self.prev_month_btn = customtkinter.CTkButton(
#             self.switch_btn_frame,
#             text="prev",
#             width=60
#             )
#         self.prev_month_btn.grid(row=0, column=0, padx=(0, 50), pady=10)
#         self.next_month_btn = customtkinter.CTkButton(
#             self.switch_btn_frame,
#             text="next",
#             width=60
#             )
#         self.next_month_btn.grid(row=0, column=1, padx=(50, 0), pady=10)

class MiniCalendarApp(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Calendar")
        self.geometry("800x600")

        # calendar data (year, month, day, etc.)
        self.current_data = date.today()
        year_label = customtkinter.CTkLabel(self, text=self.current_data.year).grid(row=0)
        year_month = customtkinter.CTkLabel(
            self,
            text=self.current_data.strftime("%B")
            ).grid(row=1)

        self.day_labels = []
        column_index = 0
        for day in WeekDays():
            self.day_labels.append(
                customtkinter.CTkLabel(self, text=day).grid(column=column_index, row=2, padx=10)
            )
            column_index += 1

        self.current_month_days_btns = []
        days_iterator = calendar.Calendar().itermonthdays(
            year=self.current_data.year,
            month=self.current_data.month
        )
        day_list = list(filter(lambda x: x != 0, days_iterator))
        row_index = 3
        column_index = date.weekday(date(
            self.current_data.year,
            self.current_data.month,
            1
        ))
        for day in day_list:
            if column_index == 7:
                column_index = 0
                row_index += 1
            self.current_month_days_btns.append(
                customtkinter.CTkButton(self, text=day, height=25, width=30).grid(
                    row=row_index, column=column_index, pady=(0, 10)
                )
            )
            column_index += 1



class WeekDays:
    def __init__(self) -> None:
        self.names = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    def __iter__(self):
        self.current_day_index = 0
        return self

    def __next__(self):
        if self.current_day_index > len(self.names) - 1:
            raise StopIteration
        else:
            day_name = self.names[self.current_day_index]
            self.current_day_index += 1
            return day_name

    def get_day_name(self, day_index):
        if day_index > 6:
            return False
        return self.names[day_index]


if __name__ == "__main__":
    MiniCalendarApp().mainloop()

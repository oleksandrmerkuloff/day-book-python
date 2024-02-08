import customtkinter
from datetime import date
import calendar


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


class CalendarSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # calendar data (year, month, day, etc.)
        self.current_date = date.today()
        self.year = self.current_date.year
        self.month = self.current_date.month

        self.fill_window()

        # Btns for switching month
        self.switch_btn_frame = customtkinter.CTkFrame(self, height=50)
        self.switch_btn_frame.grid(
            row=8,
            column=2,
            columnspan=3,
            pady=(40, 0)
            )
        self.prev_month_btn = customtkinter.CTkButton(
            self.switch_btn_frame,
            text="prev",
            width=60,
            command=self.decrease_date
            )
        self.prev_month_btn.grid(row=0, column=0, padx=(0, 50), pady=10)
        self.next_month_btn = customtkinter.CTkButton(
            self.switch_btn_frame,
            text="next",
            width=60,
            command=self.increase_date
            )
        self.next_month_btn.grid(row=0, column=1, padx=(50, 0), pady=10)

    def increase_date(self):
        self.month += 1
        if self.month > 12:
            self.year += 1
            self.month = 0
        for widget in self.winfo_children():
            widget.destroy()
        self.fill_window()

    def decrease_date(self):
        self.month -= 1
        if self.month < 0:
            self.year -= 1
            self.month = 12
        for widget in self.winfo_children():
            widget.destroy()
        self.fill_window()

    def fill_window(self):
        self.create_year_label()
        self.create_month_label()

        self.generate_weekdays_names()

        self.get_days_list()

    def create_year_label(self):
        customtkinter.CTkLabel(
            self,
            text=f"Year {self.year}"
            ).grid(row=0, column=3)

    def create_month_label(self):
        customtkinter.CTkLabel(
            self,
            text=calendar.month_name[self.month]
            ).grid(row=1, column=3)

    def generate_weekdays_names(self):
        column_index = 0
        for day in WeekDays():
            customtkinter.CTkLabel(self, text=day).grid(column=column_index, row=2, padx=10)
            column_index += 1

    def get_days_list(self):
        self.current_month_days_btns = []
        days_iterator = calendar.Calendar().itermonthdays(
            year=self.year,
            month=self.month
        )
        days_list = list(filter(lambda x: x != 0, days_iterator))
        self.create_calendar(days_list)

    def create_calendar(self, days_list):
        row_index = 3
        column_index = date.weekday(date(
            self.year,
            self.month,
            1
        ))
        for day in days_list:
            if column_index == 7:
                column_index = 0
                row_index += 1
            self.current_month_days_btns.append(
                customtkinter.CTkButton(self, text=day, height=80, width=70).grid(
                    row=row_index, column=column_index, pady=(0, 10), padx=10
                )
            )
            column_index += 1

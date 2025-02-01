print("NAME:- SANKET MAHAPATRA")
print("REGISTRATION NUMBER:- 2241013017")

import re

class Time:
    def __init__(self, time_str):
        self.time_str = time_str
        
    def is_valid(self):
        time_pattern = r"^(?:[01]?\d|2[0-3]):[0-5]?\d:[0-5]?\d$"
        if re.match(time_pattern, self.time_str):
            return True
        else:
            return False

    def convert_to_12_hour_format(self):
        if self.is_valid():
            hours, minutes, seconds = map(int, self.time_str.split(":"))
            period = "AM"
            if hours >= 12:
                period = "PM"
                if hours > 12:
                    hours -= 12
            if hours == 0:
                hours = 12
            return f"{hours:02d}:{minutes:02d}:{seconds:02d} {period}"
        else:
            return "Invalid time format. Please enter the time in HH:MM:SS format."

time_input = input("Enter time in 24-hour format (HH:MM:SS): ")
time_obj = Time(time_input)
print(time_obj.convert_to_12_hour_format())

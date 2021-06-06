# scratch code
import datetime

def translate_date(value):
        current_day = datetime.datetime.today().weekday() + 1
        weekdays = {"Monday": 1,
                    "Tuesday": 2,
                    "Wednesday": 3,
                    "Thursday": 4,
                    "Friday": 5,
                    "Saturday": 6,
                    "Sunday": 7}
        value = value.split(" ").pop(0)
        dict_subset = weekdays[value]
        current_day -
        return dict_subset
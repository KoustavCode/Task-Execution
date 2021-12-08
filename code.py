
import pandas as pd
from datetime import datetime


class TaskExecution:
    """Execution class of the Task execution logic
    """

    @staticmethod
    def second_execute(input_, current_datetime):
        current_day, current_time = current_datetime.split(" ")
        start, end, dates = (
            input_[-3],
            input_[-2],
            [i.strip() for i in input_[-1].split("and")],
        )
        status, day = TaskExecution.days_in_range(dates, current_day)
        if status:
            if TaskExecution.time_in_range(start, end, current_time):
                return "True"
            else:
                return "False"
        else:
            return f"{day} {start}"

    @staticmethod
    def days_in_range(given_days, current_day):
        try:
            week_days = [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ]
            if current_day in given_days:
                return True, ""
            else:
                given_day_indexes = [week_days.index(day) for day in given_days]
                current_day_index = week_days.index(current_day)
                day_index = [
                    index_ for index_ in given_day_indexes if index_ > current_day_index
                ]
                if day_index:
                    day_index = day_index[0]
                else:
                    day_index = min(given_day_indexes)
                return False, week_days[day_index]
        except Exception as e:
            return "Exception in days_in_range function"

    @staticmethod
    def time_in_range(start, end, now):
        try:
            start = datetime.strptime(start, '%H:%M:%S').time()
            end = datetime.strptime(end, '%H:%M:%S').time()
            now = datetime.strptime(now, '%H:%M:%S').time()
            if start <= end:
                return start <= now <= end
            else:
                return False
        except Exception as e:
            print(f"Exception in time_in_range function :: {e}")
            return False

    @staticmethod
    def first_execute(input_, current_time):
        start, end = input_[-3], input_[-2]
        now = current_time  # str(datetime.now().strftime("%H:%M:%S"))
        if TaskExecution.time_in_range(start, end, now):
            return "True"
        else:
            return "False"


if __name__ == "__main__":

    df = pd.read_csv('config.csv')
    df_list = df.values.tolist()

    TaskOB = TaskExecution()

    try:
        for event in df_list:
            current_time = input(
                "Current time in HH:MM:SS format : "
            )  # str(datetime.now().strftime("%H:%M:%S"))
            if not isinstance(event[-1], str):
                print(TaskOB.first_execute(event, current_time))
            else:
                current_day = input("Current Day : ")
                print(TaskOB.second_execute(event, f"{current_day} {current_time}"))
    except Exception as e:
        print(f"Exception in execution :{e}")

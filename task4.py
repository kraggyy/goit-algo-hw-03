from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()

        if birthday_this_year < today:
            birthday_this_year = datetime(today.year + 1, birthday.month, birthday.day).date()

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 6:
            if birthday_this_year.weekday() in [5, 6]:
                congrats_date = (birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))).strftime("%Y.%m.%d")
            else:
                congrats_date = birthday_this_year.strftime("%Y.%m.%d")

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congrats_date})

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "2024.02.03"}, #WEEKEND
    {"name": "Jane Smith", "birthday": "2024.02.01"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Birthday list of upcomming birthdays:", upcoming_birthdays)

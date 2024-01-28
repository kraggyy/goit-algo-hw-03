from datetime import datetime as dt

def get_days_from_today(input_date):
    try:
        users_date = dt.strptime(input_date, "%Y-%m-%d")
        now = dt.today()
        delta_days = now - users_date
        return delta_days.days

    except ValueError:
        print("Entered value is not suitable. Rigth format is yyyy-mm--dd", ValueError)
   

print(get_days_from_today('2005-06-24'))
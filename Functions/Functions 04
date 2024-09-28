from datetime import *

# Tag eingedeutscht per Listenreplace
def current_date_time():
    now = datetime.now()
    date_and_time = now.strftime("%A, %d.%m.%Y - %H:%M:%S")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    for day, tag in zip(weekdays, wochentage):
        date_and_time = date_and_time.replace(day, tag)
    print(date_and_time)

current_date_time()


# Tag per locale eingedeutscht
import locale
locale.setlocale(locale.LC_TIME, "de_DE") 

def current_date_time():
    now = datetime.now()
    date_and_time = now.strftime("%A, %d.%m.%Y - %H:%M:%S")
    print(date_and_time)

current_date_time()

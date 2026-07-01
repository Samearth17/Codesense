import calendar
from datetime import date, time, datetime

def get_events(cal, start_date, num_events):
    events = []
    for i in range(num_events):
        day_events = cal.itermonthdays2(start_date.year, start_date.month)
        while not day_events[0][1]:
            start_date = start_date.replace(day=(start_date.day + 1))
            day_events = cal.itermonthdays2(start_date.year, start_date.month)

        event_date = start_date.replace(day=day_events[0][0])
        events.append((event_date, day_events[0][1]))
        start_date = start_date.replace(day=(start_date.day + 1))
    return events

cal = calendar.Calendar()
start_date = date.today()
events = get_events(cal, start_date, 5)
# print out the upcoming 5 events
for event in events:
    print(event[0], event[1])
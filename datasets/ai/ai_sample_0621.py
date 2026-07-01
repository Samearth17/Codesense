import datetime

def generate_calendar(tasks, appointments):
    day = datetime.datetime.now().strftime('%A')
    calendar = {day: {}}

    for task in tasks:
        calendar[day]['tasks'] = {'name': task['name'], 'time': task['time']}

    for appointment in appointments:       
        calendar[day]['appointments'] = {'name': appointment['name'], 'time': appointment['time']}  
    return calendar

if __name__ == '__main__':
    tasks = [{'name': 'Write code', 'time': '8pm'}, {'name': 'Complete project', 'time': '9pm'}]
    appointments = [{'name': 'Meeting with Bob', 'time': '2pm'}, {'name': 'Meeting with Alice', 'time': '4pm'}]
    result = generate_calendar(tasks, appointments)
    print(result)
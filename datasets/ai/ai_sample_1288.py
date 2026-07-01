def print_schedule(working_hours, tasks):
    start = working_hours[0]
    end = working_hours[1]
    time = start

    print("| Tasks | Start | End | Duration |")
    print("| ----- | ----- | --- | -------- |")

    for task in tasks:
        task_name, duration = task
        time_start = time
        time_end = time + duration
        if time_end > end:
            print("Can not finish all tasks within given working hours")
            break
        else:
            print("| {0} | {1} | {2} | {3} |".format(task_name, time_start, time_end, duration))
            time = time + duration

working_hours = (9, 17)
tasks = [("Task 1", 2), ("Task 2", 3), ("Task 3", 4)]
print_schedule(working_hours, tasks)
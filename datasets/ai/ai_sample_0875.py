def solve_scheduling(tasks):
    # Sort tasks by their finish time
    tasks.sort(key=lambda task: task["end"])

    # Initialize the solution sequence
    sequence = [tasks[0]]

    # Loop over the rest of the tasks in order
    for curr_task in tasks[1:]:
        last_task = sequence[-1]
        if curr_task["start"] >= last_task["end"]:
            sequence.append(curr_task)

    return sequence

tasks = [{"start":3, "end":7}, {"start":1, "end":2}, {"start":6, "end":10}, {"start":8, "end":11}, {"start":12, "end":15}]
sequence = solve_scheduling(tasks)

print("The sequence of tasks is:")
for task in sequence:
    print(task)
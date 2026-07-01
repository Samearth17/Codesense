def schedule_tasks(tasks):
  scheduled_tasks = []
  tasks.sort(key=lambda x: x[1]) # sort tasks by deadline
  current_time = 0
  
  while len(tasks) > 0:
    for task in tasks:
      if current_time + task[1] <= task[2]: # check if the task can be completed before its deadline
        scheduled_tasks.append(task) # add the task to the list of scheduled tasks
        current_time += task[1] # update the current time
        tasks.remove(task) # remove the task from the list of tasks
        break # move on to the next task
  
  return scheduled_tasks

schedule_tasks([("Task A", 2), ("Task B", 1), ("Task C", 3)]); # returns [("Task B", 1), ("Task A", 2)]
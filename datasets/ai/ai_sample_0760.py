employees = [
    ['John', 45000],
    ['Jane', 50000],
    ['Michael', 60000],
    ['Josh', 40000]
]

highest_salary = 0
highest_name = ""

for name, salary in employees:
    if salary > highest_salary:
        highest_salary = salary
        highest_name = name

print("The highest-paid employee is " + highest_name + " with a salary of " + str(highest_salary))
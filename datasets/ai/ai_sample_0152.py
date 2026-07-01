import csv

def get_average_salary(filename):
  total = 0
  count = 0

  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) # skip header

    # loop through the CSV rows
    for row in csvreader:
      total += int(row[1])
      count += 1
  
  return total/count

average_salary = get_average_salary('salary.csv')
print('Average Salary: ', average_salary)

# Output: 
# Average Salary: 2000.0
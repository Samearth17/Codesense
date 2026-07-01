Develop a program in Python that will identify the number of days until a given date. An example of the code may be as follows:

from datetime import datetime

# get the current date 
current_date = datetime.now()

# get the given date 
given_date = datetime.strptime("12/25/2022", "%m/%d/%Y")

# calculate the difference 
difference = given_date - current_date

# print the result
print("Number of days until 12/25/2022: " + str(difference.days))
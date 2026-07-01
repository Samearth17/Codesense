import datetime

def calc_diff(user1, user2):
 date1 = datetime.datetime.strptime(user1, "%Y-%m-%d")
 date2 = datetime.datetime.strptime(user2, "%Y-%m-%d")
 
 days_diff = (date2 - date1).days

 years_diff = int(days_diff / 365)
 months_diff = int(days_diff % 365 / 30)
 days_diff = int(days_diff % 365 % 30)

 return years_diff, months_diff, days_diff

user1 = "1989-09-26"
user2 = "1997-03-15"

years_diff, months_diff, days_diff = calc_diff(user1, user2)

print(f"There is a difference of {years_diff} years, {months_diff} months, and {days_diff} days between the two users' birthdays.")
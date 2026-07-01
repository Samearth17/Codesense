import csv
from datetime import datetime

#open CSV file for reading
with open('source.csv', 'r') as file_in:
 #open other CSV file for writing
 with open('destination.csv', 'w', newline='') as file_out:
  reader = csv.reader(file_in)
  writer = csv.writer(file_out)

  for row in reader:
   if row[0] == "name": #skip the first row
    #write old header
    writer.writerow(row)
   else:
    #convert date format
    dt = datetime.strptime(row[1], '%m/%d/%Y').strftime('%d/%m/%Y')
    #write data with new format
    writer.writerow([row[0], dt])
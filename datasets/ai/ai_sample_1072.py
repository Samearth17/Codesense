import csv
 
class CSVProcessor:
 
 def __init__(self, path):
 self.csv_data = []
 with open(path, 'r') as csvfile:
 reader = csv.reader(csvfile)
 for row in reader:
 self.csv_data.append(row)
 
 def filter_rows(self, column, value):
 filtered = []
 for row in self.csv_data:
 if row[column] == value:
 filtered.append(row)
 return filtered
 
 def calculate_average(self, column):
 values = [float(row[column]) for row in self.csv_data]
 return sum(values) / len(values)
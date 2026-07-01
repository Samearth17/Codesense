"""
Parses a CSV and generates a new CSV that adds the total number of rows, total 
number of columns, and total amount of data for each attribute.
"""

import csv

def parse_csv(filename):
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        rows =0
        cols = 0
        data_totals = []
        for row in reader:
            rows += 1
            cols = len(row)
            for col in row:
                if len(data_totals) < cols:
                    data_totals.append([row[col],1])
                else:
                    existing_total = data_totals[cols - 1]
                    new_total = [existing_total[0] + float(row[col]), existing_total[1] + 1]
                    data_totals.append(new_total)
        #write to new csv
        with open('new_csv.csv', mode='w') as new_csv_file:
            writer = csv.writer(new_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Rows', 'Columns', 'Data Totals'])
            writer.writerow([rows, cols, data_totals])

if __name__ == '__main__':
    filename = 'test.csv'
    parse_csv(filename)
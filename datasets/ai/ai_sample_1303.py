import csv

def read_csv(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) # Skip the header

        for row in csv_reader:
            yield row

def write_csv(filename, rows):
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['A', 'C'])
        for row in rows:
            csv_writer.writerow([row[0], row[2]])

# Main
if __name__ == "__main__":
    filename = 'myfile.csv'
    rows = read_csv(filename)
    write_csv('newfile.csv', rows)
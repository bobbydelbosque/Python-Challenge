import os
import csv

file_name ="Resources/election_data.csv"
with open(file_name) as fh:
    csv_reader = csv.reader(fh)

    column_headers = next(csv_reader)

    for row in csv_reader:
        print(row)
        break
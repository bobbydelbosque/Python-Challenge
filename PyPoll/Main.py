import csv

file_name = "Resources/election_data.csv"

with open(file_name) as fh:
    csv_reader = csv.reader(fh)    
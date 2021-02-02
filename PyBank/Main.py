import csv

file_name = "Resources/election_data.csv"

results_dict = {}
total_votes = 0

with open(file_name) as fh:
    csv_reader = csv.reader(fh)

    column_headers = next(csv_reader)

    for row in csv_reader:
       cur_candidate = row[2]

import csv

file_name = "Resources/budget_data.csv"
with open(file_name) as fh:
    csv_reader = csv.reader(fh)

    
    for row in csv_reader:
        print(row)
        break 

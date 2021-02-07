import csv
import os

# Files to load and output (Remember to change these)
budget_data = os.path.join("Resources", "budget_data.csv")

months = []
net_total = []

with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for rows in csvreader:
        print(rows)

        
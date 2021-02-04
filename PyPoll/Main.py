import csv

file_name = "Resources/election_data.csv"

results_dict = {}
total_votes = 0

with open(file_name) as fh:
    csv_reader = csv.reader(fh)
    
    column_headers = next(csv_reader)

    for row in csv_reader:
        cur_candidate = row[2]
              
        #create new dict entry if doesn't exist
        if cur_candidate not in results_dict:
            results_dict[cur_candidate] = 0
        
   
        #always count
        total_votes +=1
        results_dict[cur_candidate] +=1
   
    
print(f"total votes: {total_votes}")
print(results_dict)



    
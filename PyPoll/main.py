import os
import csv

poll_csv = os.path.join('Resources', 'election_data.csv')

#define variables
votes = 0
candidates = {}
percent_C = {}
winner = ""
winner_count = 0

# Open and read csv
with open (poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    firstrow = next(csvreader)

    for row in csvreader:
        votes = votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

for key, value in candidates.items():
    percent_C[key] = round((value/votes)*100,2)

for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(percent_C[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

new_file = open("results.txt", "w")

# writing the new file
new_file.write("Election Results \n")
new_file.write("------------------------------------- \n")
new_file.write("Total Votes: " + str(votes) + "\n")
new_file.write("------------------------------------- \n")
for key, value in candidates.items():
    new_file.write(key + ": " + str(percent_C[key]) + "% (" + str(value) + ") \n")
new_file.write("------------------------------------- \n")
new_file.write("Winner: " + winner + "\n")
new_file.write("------------------------------------- \n")

import os

import csv

main_csv = os.path.join("Resources", "budget_data.csv")

total_mos = 0
total_net = 0
max_c = 0
min_c = 0
pl_ratio = 0
old_pl = 0
percent_c = 0
diff = 0
diflist = []


# Open and read csv
with open(main_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #grab first row
    firstrow = next(csvreader)
    #grab prev value from first row
    old_pl = int(firstrow[1])

    for row in csvreader:  
        total_mos = total_mos + 1

        pl_ratio = pl_ratio + int(row[1])

        percent_c = int(row[1])

        diff = percent_c - old_pl

        diflist.append(diff)

        old_pl = percent_c

        if percent_c > max_c:
            max_c = percent_c
            max_month = row[0]

        if percent_c < min_c:
            min_c = percent_c
            min_month = row[0]

listaverage = (sum(diflist) / total_mos)
print("Financial Review")
print(f"Total Months: {total_mos}")
print(f"Total: {pl_ratio}")
print(f"Average Change: {listaverage}")
print(f"Greatest Increase in Profits: {max_c}")
print(f"Greatest Decrease in Profits: {min_c}")

new_file = open("bankresults.txt","w")

new_file.write("Financial Analysis \n")
new_file.write("-------------------------------------------- \n")
new_file.write(f"Total Months: {total_mos} \n")
new_file.write(f"Total: {pl_ratio} \n")
new_file.write(f"Average Change: {listaverage} \n")
new_file.write(f"Greatest Increase in Profits: {max_c} \n")
new_file.write(f"Greatest Decrease in Profits: {min_c} \n")

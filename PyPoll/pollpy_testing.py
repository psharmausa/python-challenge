import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# declare dictionary
pollDict = {}
# set the counter to 0
rnum = 0

# Open and read csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the header
    next(csvreader) 

# Count number of the rows and it going to show the count(rnum) of the name of candidate
    for row in csvreader:
        rnum +=1
        
        if row[2] in pollDict:
            pollDict[row[2]] += 1
        else:
            pollDict[row[2]] = 1
            print(row)
    print(row)
    # print(rnum)
    # print(f'Total Votes: {rnum}')
    print('-------------------------------------------')

# This will allow us to create file paths across operating systems
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
        
    total_votes=rnum
    print('-------------------------------------------')
# total no. of votes by setting by the counter rnum
    print(f'Total Votes: {total_votes}')
    print('-------------------------------------------')

# Now print the requested calculation:-
# A complete list of candidates who received votes
#The percentage of votes each candidate won
    for word in pollDict:
        print (f'{word}:  {round((pollDict[word]/rnum*100),2)}00% ({int(pollDict[word])})')
    
#The winner of the election based on popular vote.
    max_value = 0
    winner = ""
    for i in pollDict:
        votes=pollDict[i]
        if votes > max_value:
            max_value = votes
            winner = i
            print('-------------------------------------------')
            print(f'Winner:         {i}')
            print('-------------------------------------------')


# write the file in text file and w is used for replacing existing file
f = open("output_PyPoll.txt", "w")
print('-------------------------------------------', file=f)
print(f'Total Votes: {int(total_votes)}',file=f)
print('-------------------------------------------', file=f)
for word in pollDict:
    print (f'{word}:  {round((pollDict[word]/rnum*100),2)}00% ({int(pollDict[word])})', file=f)
    
    
max_value = 0
winner = ""
for i in pollDict:
        votes=pollDict[i]
        if votes > max_value:
            max_value = votes
            winner = i
            print('-------------------------------------------',file=f)
            print(f'Winner:         {i}',file=f)
            print('-------------------------------------------',file=f)
f.close()
   

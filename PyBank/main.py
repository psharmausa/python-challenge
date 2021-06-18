# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# create array for dates , total and entire change in prices -Lists
dates =  []
total =  []
change = []

 # Open and read csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip the header
    next(csvreader) 

# Read each row of data after the header  '
    for row in csvreader: 
        dates.append(row[0]) 
        total.append(int(row[1]))

# Total number of months(count no. of elements in the list for total  or dates count )
# Total Profit & Loss ;               
        total_mths=len(total)
        total_pl=int(sum(total))
    
# The average of the changes over the entire period
    for i in range(1, len(total)): 
        change.append(total[i] - total[i-1])

# The average of the changes in "Profit/Losses" over the entire period
        avg_chng = round(sum(change) / len(change),2)

# The greatest increase in profits (date and amount) over the entire period
        max_chng = max(change)
# The greatest decrease in losses (date and amount) over the entire period
        min_chng = min(change)

# Through index get location of the date and get date value from dates array 
        max_dt_chng = dates[change.index(max_chng)]
        min_dt_chng = dates[change.index(min_chng)]

print("------------------------------------------------------------------------------")
print("Financial Analysis")
print("-------------------------------------------------------------------------------")
print(f'Total Months: {total_mths}')
print(f'Total: ${total_pl}')
print(f'Average Change: ${avg_chng}')
print(f'Greatest Increase in Profits: {max_dt_chng}  (${int(max_chng)})')
print(f'Greatest Decrease in Profits: {min_dt_chng}  (${int(min_chng)})')

# write the file in text file and w is used for replacing existing file
f = open("output.txt", "w")
print("----------------------------------------------------------------------------", file=f)
print("Financial Analysis", file=f)
print("-----------------------------------------------------------------------------", file=f)
print(f'Total Months: {total_mths}', file=f)
print(f'Total: ${total_pl}', file=f)
print(f'Average Change: ${avg_chng}', file=f)
print(f'Greatest Increase in Profits: {max_dt_chng}  (${int(max_chng)})', file=f)
print(f'Greatest Decrease in Profits: {min_dt_chng}  (${int(min_chng)})', file=f)
f.close()
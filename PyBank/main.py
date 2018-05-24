import csv
import os 

csvpath = os.path.join("/Users/alex/Desktop/budget_data_1.csv")

totalMonths = 0 
totalRevenue = 0
changeRevenue = 0
#monthList = []
#revList = []
#combinedList = []
#smallestChange = 0
#largestChange = 0

#open csv and read it, skipping the header line
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    reader.__next__()
    
    for row in reader:
        totalRevenue += int(row[1])
        if not "":
            totalMonths += 1
        #monthList.append(row[0])
        #revList.append(row[1])
       
    changeRevenue = ("Average Revenue Change: " + "$" + str(int(totalRevenue/totalMonths)))
    totalMonths = ("Total Months: " + str(totalMonths))
    totalRevenue =  ("Total Revenue: " + "$" + str(totalRevenue)) 
   
    #print("Total Months: " + str(totalMonths))
    #print("Total Revenue: " + "$" + str((totalRevenue))
    #print("Average Revenue Change: " + "$" + str(changeRevenue))

with open("output.txt", 'w') as textfile:
    textfile.write(totalMonths + "\n")
    textfile.write(totalRevenue + "\n")
    textfile.write(changeRevenue)

# /create variables that count sum of months, sum of revenue
# /create a function that loops through columns 
# /loop through the revenue column and create a variable that += revenue 
# /average change in revenue will divide total revenue/total months
# greatest increase and decreases in revenue month over month


#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period


#As an example, your analysis should look similar to the one below:

#Financial Analysis
#----------------------------
#Total Months: 25
#Total Revenue: $1241412
#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)

#Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these 
#-- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.


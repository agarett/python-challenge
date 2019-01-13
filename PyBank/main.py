import csv
import os 

csvpath = os.path.join("Desktop/budget_data_1.csv")

totalMonths = 0 
totalRevenue = 0
changeRevenue = []
date = []

#open csv and read it, skipping the header line

with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")   
    reader.__next__()
    
    #loop through each row and append the months to a list. 
    for row in reader:
        date.append(row[0])

        #calculate sum of revenue and total months 
        totalRevenue += int(row[1])
        if not "":
            totalMonths += 1

            #subtract the previous row from the current row 
            if totalMonths == 1:
                priorRevenue = int(row[1])
            else:
                change = (int(row[1]) - int(priorRevenue))
                changeRevenue.append(change)
            
            #reset prior revenue to the new row value
            priorRevenue = row[1]

#assign average revenue change and sum of months and revenue      
avgChangeRevenue = ("Average Revenue Change: " + "$" + str(int(totalRevenue/totalMonths)))
totalMonths = ("Total Months: " + str(totalMonths))
totalRevenue =  ("Total Revenue: " + "$" + str(totalRevenue))

#calculate the largest Revenue changes from the changeReveue list
largestIncrease = max(changeRevenue)
largestDecrease = min(changeRevenue)

increaseIndex = (changeRevenue.index(max(changeRevenue))) + 1 
decreaseIndex = (changeRevenue.index(min(changeRevenue))) + 1

increaseMonth = date[increaseIndex]
decreaseMonth = date[decreaseIndex]

greatestIncrease = ("Greatest Increase in Revenue: " + str(increaseMonth) + " ($" + str(largestIncrease) + ")")
greatestDecrease = ("Greatest Decrease in Revenue: " + str(decreaseMonth) + " ($" + str(largestDecrease) + ")")

#print results to terminal
print("Financial Analysis")
print("----------------------------")
print(totalMonths)
print(totalRevenue)
print(avgChangeRevenue)
print(greatestIncrease)
print(greatestDecrease)

#print results to text file 
with open("output1.txt", 'w') as textfile:
    textfile.write("Financial Analysis" + "\n")
    textfile.write("----------------------------" + "\n")
    textfile.write(totalMonths + "\n")
    textfile.write(totalRevenue + "\n")
    textfile.write(avgChangeRevenue + "\n")
    textfile.write(greatestIncrease + "\n")
    textfile.write(greatestDecrease)

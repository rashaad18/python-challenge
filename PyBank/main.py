# PyBank main file 
#imports
import os
import csv

# Set the path for csv file
csv_path = os.path.join("..", "Resources","budget_data.csv")

#open csv file
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    rowCount = 0
    for row in csv_reader:
        print(row[0] + "   " + row[1])
        rowCount = rowCount + 1
    rowCount = rowCount - 1
# print output to console with all analysis data
print("Financial Analysis")
print("-----------------------")
print("Total Months : " + str(rowCount))
print("Total : $")
print("Average  Change: ")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")
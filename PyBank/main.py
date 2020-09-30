# PyBank main file 
#imports
import os
import csv

rowCount = 0
totalProfitLoss = 0
average = 0
greatest_temp = {
    "month" : "",
    "money" : 0
    }
decreased_temp = {
    "month" : "",
    "money" : 0
    }

# Set the path for csv file
csv_path = os.path.join("..", "Resources","budget_data.csv")

#open csv file
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # iterates through the dataset
    for row in csv_reader:
       # print(row[0] + "   " + row[1])
        if(row[1] != "Profit/Losses"):
            totalProfitLoss = totalProfitLoss + int(row[1])
            if(int(row[1]) > int(greatest_temp["money"])):
                greatest_temp["month"] = row[0]
                greatest_temp["money"] = int(row[1])
            if(int(row[1]) < int(decreased_temp["money"])):
                decreased_temp["month"] = row[0]
                decreased_temp["money"] = int(row[1])
        
        # gets the number of rows in the dataset
        rowCount = rowCount + 1
    
    #subtracts the header row from the count to get the number of rows in the dataset
    rowCount = rowCount - 1
   
    # gets the average of the dataset
    average = int(totalProfitLoss/rowCount)

# Creates text file with data output from data analysis
file_write_path = os.path.join("..", "Analysis","budget_data_finshed_final.txt")
with open(file_write_path, "a") as data_file:
    data_file.write("Financial Analysis\n")
    data_file.write("-----------------------\n")
    data_file.write("Total Months : " + str(rowCount) + "\n")
    data_file.write("Total : $" + str(totalProfitLoss) + "\n")
    data_file.write("Average  Change: " + str(average) + "\n")
    data_file.write("Greatest Increase in Profits: " + str(greatest_temp["month"]) + " ($" + str(greatest_temp["money"]) + ")\n" )
    data_file.write("Greatest Decrease in Profits: "  + str(decreased_temp["month"]) + " ($" + str(decreased_temp["money"]) + ")\n")
    data_file.close

# print output to console with all analysis data
print("\nFinancial Analysis")
print("-----------------------")
print("Total Months : " + str(rowCount))
print("Total : $" + str(totalProfitLoss))
print("Average  Change: " + str(average))
print("Greatest Increase in Profits: " + str(greatest_temp["month"]) + " ($" + str(greatest_temp["money"]) + ")" )
print("Greatest Decrease in Profits: "  + str(decreased_temp["month"]) + " ($" + str(decreased_temp["money"]) + ")\n")
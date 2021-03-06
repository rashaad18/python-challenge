# Main for PyPoll
# imports
import os
import csv

# variables & list
canidates = ["Khan","Correy", "Li", "O'Tooley"]
khanCount = 0
correyCount = 0
liCount = 0
oTooleyCount = 0
total_votes = 0
# funtion that returns the canidates percentage of votes
def getCanidatePercentage(canidate_count,total_Votes):
    return canidate_count / total_Votes * 100

#open file location of csv
csv_path = os.path.join("..","Resources","election_data.csv")
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # iterates through the dataset and adds a count to the canidate pulled from each row
    for row in csv_reader:
       if(row[2] == "Khan"):
           khanCount = khanCount + 1
       elif(row[2] == "Correy"):
            correyCount = correyCount + 1
       elif(row[2] == "Li"):
            liCount = liCount + 1
       elif(row[2] == "O'Tooley"):
            oTooleyCount = oTooleyCount + 1
     
       
# get the total amount of votes
total_votes = khanCount + correyCount + liCount + oTooleyCount
    
# each canidates percentage of votes using get function
khan_percent = round(getCanidatePercentage(khanCount,total_votes),2)
correy_percent = round(getCanidatePercentage(correyCount,total_votes),2)
li_percent = round(getCanidatePercentage(liCount,total_votes),2)
oTooley_percent = round(getCanidatePercentage(oTooleyCount,total_votes),2)
winner = ""

# Checks to see whos poll percentage is higher so a winner can be selected and displayed
if((khan_percent > correy_percent) & (khan_percent > li_percent) & (khan_percent > oTooley_percent)):
    winner = canidates[0]
elif((correy_percent > khan_percent) & (correy_percent > li_percent) & (correy_percent > oTooley_percent)):
    winner = canidates[1]
elif((li_percent > khan_percent) & (li_percent > correy_percent) & (li_percent > oTooley_percent)):
    winner = canidates[2]
elif((oTooley_percent > khan_percent) & (oTooley_percent > li_percent) & (oTooley_percent > correy_percent)):
    winner = canidates[3]

# Creates text file with data output from data analysis
file_write_path = os.path.join("..", "Analysis","electrion_data_finshed.txt")
with open(file_write_path, "w") as data_file:
    data_file.write("Election Results\n")
    data_file.write("---------------------\n")
    data_file.write("Total Votes: " + str(total_votes) +"\n")
    data_file.write("---------------------\n")
    data_file.write("Khan: " + str(khan_percent) + "% (" + str(khanCount) + ")\n")
    data_file.write("Correy: " + str(correy_percent) + "% (" + str(correyCount) + ")\n")
    data_file.write("Li: " + str(li_percent) + "% (" + str(liCount) + ")\n")
    data_file.write("O'Tooley: " + str(oTooley_percent) + "% (" + str(oTooleyCount) + ")\n")
    data_file.write("---------------------\n")
    data_file.write("Winner: " + winner + "\n")
    data_file.write("---------------------\n")

#print output to console  of election results      
print("Election Results")
print("---------------------")
print("Total Votes: " + str(total_votes))
print("---------------------")
print("Khan: " + str(khan_percent) + "% (" + str(khanCount) + ")")
print("Correy: " + str(correy_percent) + "% (" + str(correyCount) + ")")
print("Li: " + str(li_percent) + "% (" + str(liCount) + ")")
print("O'Tooley: " + str(oTooley_percent) + "% (" + str(oTooleyCount) + ")")
print("---------------------")
print("Winner: " + winner)
print("---------------------")

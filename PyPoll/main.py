import os 
import csv
# import dependencies since we are using csv files and we need os for path guidance

PyPoll_Data = os.path.join('.', 'Resources', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')
#pyPoll data is the path variable

Total_Votes = 0
Khan_Votes = 0
Correy_Votes = 0
Li_Votes = 0
OTooley_Votes = 0
candidates = []
Vote_Counts = []
winner_list = []

# setting some variables to zero and will assigning counters to them to add up votes
# winner and vote counts are open lists, where we will append candidate name and their votes.

with open(PyPoll_Data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',') # splits columns based on comma
    csvheader = next(csvreader) # skips the header row

    for row in csvreader:
        Total_Votes = Total_Votes + 1 # counts all the votes tallied 

        if str(row[2]) == "Khan":        # if statement -  counts based on name match
            Khan_Votes = Khan_Votes + 1
            Khan_Percentage = round(((Khan_Votes / Total_Votes) * 100),3)
        elif str(row[2]) == "Correy":      # if statement -  counts based on name match
            Correy_Votes = Correy_Votes + 1
            Correy_Percentage = round(((Correy_Votes / Total_Votes) * 100),3)
        elif str(row[2]) == "Li":            # if statement -  counts based on name match
            Li_Votes = Li_Votes + 1
            Li_Percentage = round(((Li_Votes / Total_Votes) * 100),3)
        elif str(row[2]) == "O'Tooley":               # if statement -  counts based on name match
            OTooley_Votes = OTooley_Votes + 1
            OTooley_Percentage = round(((OTooley_Votes / Total_Votes) * 100),3)

candidates.append("Khan")   # append all names into a list called candidates
candidates.append("Correy")
candidates.append("Li")
candidates.append("O'Tooley")

Vote_Counts.append(Khan_Votes)       # append the votes to a list called Vote_Counts
Vote_Counts.append(Correy_Votes)     # we could use dict to combine both list instead of zip
Vote_Counts.append(Li_Votes)
Vote_Counts.append(OTooley_Votes)

combined_data = list(zip(candidates, Vote_Counts))   # combines both lists using zip function

for name in combined_data:              #iterates through list 
   if max(Vote_Counts) == name[1]:      # finds the max votes associated with the candidate name
        winner_list.append(name[0])     # adds the winners name in winner list 

winner = winner_list[0]                 
    
#prints results
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(Total_Votes))
print("-----------------------")
print(f"Khan: {Khan_Percentage}% ({Khan_Votes})")
print(f"Correy: {Correy_Percentage}% ({Correy_Votes})")
print(f"Li: {Li_Percentage}% ({Li_Votes})")
print(f"O'Tooley: {OTooley_Percentage}% ({OTooley_Votes})")
print("-----------------------")
print("Winner : " + str(winner))
print("-----------------------")

with open('PyPoll-Analysis.txt', 'w') as text:
    text.write("Election Results" + "\n")
    text.write("_________________________\n")
    text.write(f"Total Votes: {Total_Votes} \n")
    text.write("_________________________\n")
    text.write(f"Khan: {Khan_Percentage}% ({Khan_Votes})\n")
    text.write(f"Correy: {Correy_Percentage}% ({Correy_Votes})\n")
    text.write(f"Li: {Li_Percentage}% ({Li_Votes})\n")
    text.write(f"O'Tooley: {OTooley_Percentage}% ({OTooley_Votes})\n")
    text.write("_________________________\n")
    text.write(f"Winner : {winner} \n")
    text.write("_________________________\n")
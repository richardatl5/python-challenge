import os
import csv

PyPoll_Data = os.path.join('.', 'Resources', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

Total_Votes = 0
Khan_Votes = 0
Correy_Votes = 0
Li_Votes = 0
OTooley_Votes = 0
candidates = []
Vote_Counts = []
winner_list = []

with open(PyPoll_Data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csvheader = next(csvreader)

    for row in csvreader:
        Total_Votes = Total_Votes + 1

        if str(row[2]) == "Khan":
            Khan_Votes = Khan_Votes + 1
            Khan_Percentage = round(((Khan_Votes / Total_Votes) * 100),3)
        elif str(row[2]) == "Correy":
            Correy_Votes = Correy_Votes + 1
            Correy_Percentage = round(((Correy_Votes / Total_Votes) * 100),3)
        elif str(row[2]) == "Li":
            Li_Votes = Li_Votes + 1
            Li_Percentage = round(((Li_Votes / Total_Votes) * 100),3)
        elif str(row[2]) == "O'Tooley":
            OTooley_Votes = OTooley_Votes + 1
            OTooley_Percentage = round(((OTooley_Votes / Total_Votes) * 100),3)

candidates.append("Khan") 
candidates.append("Correy")
candidates.append("Li")
candidates.append("O'Tooley")

Vote_Counts.append(Khan_Votes)
Vote_Counts.append(Correy_Votes)
Vote_Counts.append(Li_Votes)
Vote_Counts.append(OTooley_Votes)

combined_data = list(zip(candidates, Vote_Counts)) 

for name in combined_data:
   if max(Vote_Counts) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]
    

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
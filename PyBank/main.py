import os # import os library to generate path to CSV file 
import csv # csv liberary to read csv file

budget_data = os.path.join('.', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv') #setting the path to the file

TotalMonths = 0
TotalRevenue = 0
TotalRevChange = 0
PreviousRev = 0
GreatestIncr = 0
GreatestDec = 0
AvgChange = 0
GreatestDate = 0
GreatestDecDate = 0

with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  # using reader and not writer becasue we are not making changes to the data
    csv_header = next(csvreader)

    for row in csvreader:

        TotalMonths = TotalMonths + 1 # counts all the rows, since each row is limited to one month

        TotalRevenue = TotalRevenue + int(row[1])

        revIncrease = int(row[1]) - PreviousRev
        TotalRevChange = TotalRevChange + revIncrease
        PreviousRev =int(row[1])
        AvgChange = round(TotalRevChange/TotalMonths,2)

        if(revIncrease > GreatestIncr):
            GreatestIncr = revIncrease 
            GreatestDate = row[0]
        if(revIncrease < GreatestDec):
            GreatestDec = revIncrease
            GreatestDecDate = row[0]

print("Financial Analysis")

print("_________________________________")

print("Total Months: " + str(TotalMonths))
print("Total Revenue: $" + str(TotalRevenue))
print("Average Change: $" + str(AvgChange))
print(f" Greatest Increase in Profits:   {GreatestDate} (${GreatestIncr})")
print(f" Greatest Decrease in Profits:   {GreatestDecDate} (${GreatestDec})")

with open('financial-analysis.txt', 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("_________________________\n")
    text.write("Total Months: " + str(TotalMonths) + "\n")
    text.write("Total Revenue: $" + str(TotalRevenue) + "\n")
    text.write("Average Change: $" + str(AvgChange) + "\n")
    text.write(f" Greatest Increase in Profits:   {GreatestDate} (${GreatestIncr})\n")
    text.write(f" Greatest Decrease in Profits:   {GreatestDecDate} (${GreatestDec})\n")





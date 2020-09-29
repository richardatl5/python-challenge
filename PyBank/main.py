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

        TotalRevenue = TotalRevenue + int(row[1])  # adds up the column total of profits/losses

        revIncrease = int(row[1]) - PreviousRev  # subtracts current row from the previous row and stores value in variable
        TotalRevChange = TotalRevChange + revIncrease # adds up all the revenue change 
        PreviousRev =int(row[1])
        AvgChange = round(TotalRevChange/TotalMonths,2) # not sure how to accurately discard the first row on a loop

        if(revIncrease > GreatestIncr):   # as it loops it stores the greatest rev compared to the previous rev
            GreatestIncr = revIncrease 
            GreatestDate = row[0]
        if(revIncrease < GreatestDec): # as it loops it stores lowest decrease compared to the previous
            GreatestDec = revIncrease
            GreatestDecDate = row[0]

print("Financial Analysis")   # prints all the variables, concatenated with string

print("_________________________________")

print("Total Months: " + str(TotalMonths))
print("Total Revenue: $" + str(TotalRevenue))
print("Average Change: $" + str(AvgChange))
print(f"Greatest Increase in Profits:   {GreatestDate} (${GreatestIncr})")  # use of f-string for simplicity and speed
print(f"Greatest Decrease in Profits:   {GreatestDecDate} (${GreatestDec})")

with open('financial-analysis.txt', 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("_________________________\n")
    text.write("Total Months: " + str(TotalMonths) + "\n")
    text.write("Total Revenue: $" + str(TotalRevenue) + "\n")
    text.write("Average Change: $" + str(AvgChange) + "\n")
    text.write(f"Greatest Increase in Profits:   {GreatestDate} (${GreatestIncr})\n")
    text.write(f"Greatest Decrease in Profits:   {GreatestDecDate} (${GreatestDec})\n")





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


profit = []

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







print("Financial Analysis")

print("_________________________________")

print("Total Months: " + str(TotalMonths))
print("Total Revenue: $" + str(TotalRevenue))
print("Average Change: $" + str(AvgChange))







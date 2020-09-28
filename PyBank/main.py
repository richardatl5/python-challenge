import os # import os library to generate path to CSV file 
import csv # csv liberary to read csv file

budget_data = os.path.join('.', 'Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv') #setting the path to the file

TotalMonths = 0
TotalRevenue = 0
PnL = []

profit = []

with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  # using reader and not writer becasue we are not making changes to the data
    csv_header = next(csvreader)

    for row in csvreader:
        TotalMonths = TotalMonths + 1 # counts all the rows, since each row is limited to one month

        profit.append(row[1])
        TotalRevenue = TotalRevenue + int(row[1])



print("Financial Analysis")

print("_________________________________")

print("Total Months: " + str(TotalMonths))
print("Total Revenue: $" + str(TotalRevenue))







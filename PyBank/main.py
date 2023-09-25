#import the OS Module
import os

#The module for reading csv files
import csv

csv_budget = os.path.join('Resources', 'budget_data.csv')

#Create lists to store data
months = 0
net_profit = []

with open (csv_budget) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    
  # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        months +=1
        net_profit.append(int(row[1]))

with open('BudgetAnalysis.txt', 'w') as output_file:



    print("Financial Analysis")

    print(f"Months: {months}")
    output_file.write(f"Financial Analysis\nMonths: {months} \n")

    print(f"Net Profit:$ {sum(net_profit)}")
    output_file.write(f"Net Profit:$ {sum(net_profit)}")
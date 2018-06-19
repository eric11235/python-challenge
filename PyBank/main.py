# For all calculations in this assignment, the column in budget_data.csv labeled 'Revenue' is assumed to actually be the monthly profit or loss

#Import CSV module and OS modules

import os
import csv

# Path to collect data from the Resources folder
dataCSV = os.path.join('Resources', 'budget_data.csv')

# Clear the screen for enhanced user visiblity
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('Financial Analysis')
print()
print('--------------------------')
print()

# Open the CSV file --> Calculate total months in the dataset...note there is a header row in the dataset

with open(dataCSV, 'r', newline = '') as datafile:
    totalrows = len(datafile.readlines())
    totalmonths = totalrows - 1
    print("Total Months: ",totalmonths)

# Open the CSV file --> Calculate total net amount of Profits/Losses over the entire period

with open(dataCSV, 'r', newline = '') as datafile:
    csvreader = csv.reader(datafile, delimiter = ',')
    headerline = next(datafile)
    totalprofit = 0
    for row in csv.reader(datafile):
        totalprofit += int(row[1])
    print("Total: $",totalprofit)

# Open the CSV file --> Calculate average change in Profit/Losses between months over the entire period
    # Read the profit & loss data (from Date column) into a list called date_list and (from Revenue column) into a list called profit_loss_list
with open(dataCSV, newline='') as datafile:
    headerline = next(datafile)
    date_list = []
    profit_loss_list = []
    for row in csv.reader(datafile):
        date_item = row[0]
        date_list.append(date_item)
        profit_loss_item = int(row[1])
        profit_loss_list.append(profit_loss_item)

    # Create two new lists from the profit_loss_list --> p_l_list_first and p_l_list_last that excludes the first and last elements, respectively
p_l_list_first = profit_loss_list[1:]
p_l_list_last = profit_loss_list[:-1]

    # Subtract the p_l_list_last from the p_list_first and place results in a new list, monthly_change_profit_list, which represents the monthly change in profit
monthly_change_profit_list = [first - last for first,last in zip(p_l_list_first,p_l_list_last)]

# Calculate the average of the monthly change in profits
average = sum(monthly_change_profit_list) / float(len(monthly_change_profit_list))
print("Average Change: $",average)

# Search the monthly_change_profit_list created above for the Max value and identify the nth month in which this max profit change occurs
max_profit_increase = max(monthly_change_profit_list)
month_max_profit_increase = monthly_change_profit_list.index(max_profit_increase)
print("Greatest Increase in Profits:",date_list[month_max_profit_increase + 1],"($",max_profit_increase,")")

# Search the monthly_change_profit_list created above for the Min value and identify the nth month in which this min profit change occurs
min_profit_increase = min(monthly_change_profit_list)
month_min_profit_increase = monthly_change_profit_list.index(min_profit_increase)
print("Greatest Decrease in Profits:",date_list[month_min_profit_increase + 1],"($",min_profit_increase,")")

# Output print statements to a text file
with open('Output_Print.txt', 'w') as f:
    print('Financial Analysis', file=f)
    print('--------------------------', file=f)
    print('\n', file=f)
    print("Total Months: ",totalmonths, file=f)
    print("Total: $",totalprofit, file=f)
    print("Average Change: $",average, file=f)
    print("Greatest Increase in Profits:",date_list[month_max_profit_increase + 1]," $",max_profit_increase, file=f)
    print("Greatest Decrease in Profits:",date_list[month_min_profit_increase + 1]," $",min_profit_increase, file=f)

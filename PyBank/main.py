## PyBank
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#The dataset is composed of two columns: `Date` and `Profit/Losses`
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #Read the header row first 
    #csv_header = next(csvreader)
    #Skip the header row 
    csv_header = next(csvreader, None)

#create a Python script that analyzes the records to calculate each of the following:

    #The total number of months included in the dataset
    month = 0
    total_amt = 0
    months = []
    revenue = []
    net_change = []

    for row in csvreader:
        month = month + 1
        months.append(row[0])
  
    # #The net total amount of "Profit/Losses" over the entire period
        total_amt = total_amt + float(row[1])
        revenue.append(float(row[1]))


    #The average of the changes in "Profit/Losses" over the entire period
    for i in range(1,len(revenue)):
        net_change.append(revenue[i] - revenue[i-1])   
        average = round(sum(net_change)/len(net_change), 2)

    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
        max_net_change_date = str(months[net_change.index(max(net_change))])
        min_net_change_date = str(months[net_change.index(min(net_change))])
        
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# Specify the file to write to
# Open the file using "write" mode. Specify the variable to hold the contents
    with open("PyBank_output.txt", "w") as txtfile:
        txtfile.write(f"Financial Analysis \n")
        txtfile.write(f"Total Net Amount: ${total_amt} \n")
        txtfile.write(f"Average Change: ${average} \n")
        txtfile.write(f"Greatest Increase in Profits: {max(net_change)} \n")
        txtfile.write(f"Greatest Decrease in Profits: {min(net_change)} \n")
        txtfile.close()

    print("Financial Analaysis")
    print("------------------------------")
    print(f"Total Months: {month}") 
    print(f"Total Net Amount: ${total_amt}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {max_net_change_date} ({max(net_change)})")
    print(f"Greatest Decrease in Profits: {min_net_change_date} ({min(net_change)})")


    #   As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```
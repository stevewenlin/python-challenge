# import modules 
import os 
import csv

# set path for csv file to load from Resources  
bank_csv = os.path.join("Resources", "budget_data.csv")
# set path for text file to output to Analysis 
bank_text = os.path.join("Analysis", "PyBank_analysis.txt")

# creating lists to store data 
date = []
profit = []
monthly_change = [] 

# assigning variables for count  

total_profit = 0 
total_change_profit = 0 
beginning_profit = 0 

# read bank_csv that is the pybank_budget_data.csv & skip the header with next 
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:

        # calculating total month
        date.append(row[0])
        
        # calculating total profit 
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
       
        # calculating average monthly change in profit 
        final_profit = int(row[1])
        monthly_change_profit = final_profit - beginning_profit

        # adding monthly change into a list 
        monthly_change.append(monthly_change_profit)
        total_change_profit = total_change_profit + monthly_change_profit
        beginning_profit = final_profit 

        # calculating average change in profit 
        average_change_profit = (total_change_profit/len(date))

        # calculating greatest increase/decrease via max and min for change in profits + dates via index  
        greatest_increase_profit = max(monthly_change) 
        greatest_decrease_profit = min(monthly_change)

        greatest_increase_date = date[monthly_change.index(greatest_increase_profit)]
        greatest_decrease_date = date[monthly_change.index(greatest_decrease_profit)]

output =(
    f'Financial Analysis\n' 
    f'--------------------------------\n'
    f'Total Months: {str(len(date))}\n' 
    f'Total Profits: ${str(total_profit)}\n'
    f'Average Change: ${str(int(average_change_profit))}\n'
    f'Greatest Increase in Profits: {str(greatest_increase_date)} $ {str(greatest_increase_profit)}\n'
    f'Greatest Decrease in Profits: {str(greatest_decrease_date)} $ {str(greatest_decrease_profit)}\n'
)

print(output)

# writting on text file 
with open(bank_text, "w") as text:
    text.write(output)
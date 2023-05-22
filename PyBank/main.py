import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

# instantiate variables
total_months = 1
# initiate variables
net_profit_and_loss = 0
# initiate variables- list to store data
profit_loss_change_list = []
prev_profit_loss = 0



with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # skip the first row for profit loss calculation
    first_row = next(csvreader)
    # add first row's pl to net pl
    net_profit_and_loss += int(first_row[1])
    


    for row in csvreader:
        #total_months = total_months + 1
        profit_loss = int(row[1])
        change = profit_loss - prev_profit_loss
        profit_loss_change_list.append(change)
        prev_profit_loss = int(first_row[1])
        total_months+=1
        net_profit_and_loss+=profit_loss
average = sum(profit_loss_change_list)/total_months  
min= min(profit_loss_change_list)
max= max(profit_loss_change_list)
result = (f'profit increase: {max}\n'
        f'profit_loss: {min}\n'
        f'average:{average}\n'
    f'Total Months: {total_months}\n'
    f'Net Profit Loss: {net_profit_and_loss}\n'
)

print(result)
# write result to file

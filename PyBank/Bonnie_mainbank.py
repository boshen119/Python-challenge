#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies
import os
import csv


# In[ ]:


# path to data worksheet
# budget_csv = os.path ("..", "PyBank", "budget_data.csv")


# In[ ]:


# setting variables 
total_months = 0
total_profit_loss = 0
net_change = []
month_change= []
greatest_increase = 0
greatest_decrease = 0


# In[ ]:


budget_file = open("budget_data.csv", "r")


# In[ ]:


print(budget_file)


# In[ ]:


csvreader = csv.reader(budget_file, delimiter= ",")


# In[ ]:


csv_header = next(csvreader)
first_row = next(csvreader)
total_months = total_months + 1
total_profit_loss = total_profit_loss + int(first_row[1])
previous_profit_loss = int(first_row[1])


# In[ ]:


# for row in csvreader:
#     print(row[1])


# In[ ]:


print(csv_header)


# In[ ]:


for row in csvreader:
    total_months = total_months + 1
    total_profit_loss = total_profit_loss + int(row[1])
    change = int(row[1]) - previous_profit_loss
    previous_profit_loss = int(row[1])
    net_change = net_change + [change]
    month_change = month_change + [row[0]]
        
        
# if (previous_profit_loss + int(row[1]))> previous_profit_loss:
    #if change is bigger than previous change that will be your greatest increase
    #if change is less than previous change that will be your greatest decrease
    
        
# for greatest_increase in net_change:
    if change > greatest_increase:
        greatest_increase_month = row[0]
        greatest_increase_value = change
        
    if change < greatest_decrease:
        greatest_decrease_month = row[0]
        greatest_decrease_value = change
        
# print(greatest_increase)


# In[ ]:


print(total_months)
print(total_profit_loss)
print(net_change)


# In[ ]:


print(len(net_change))


# In[ ]:


average = sum(net_change)/len(net_change)
avg = print(round(average,2))


# In[ ]:


# avg_round = print(round(avg,2))


# In[ ]:


def financial_analysis():
    print("Financial_Analysis")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_profit_loss}")
    print(f"Average Change: ${average:.2f}")
    print(f"Greatest Increase: {greatest_increase_month} ${greatest_increase_value}")
    print(f"Greatest Decrease: {greatest_decrease_month} ${greatest_decrease_value}")
  


# In[ ]:


financial_analysis()


# In[ ]:


# output_path = os.path.join(".", "PyBank", "PyBank_results.txt")
#output()


# In[ ]:


output = (
   f"\nFinancial_Analysis\n"
   f"Total Months: {total_months}\n"
   f"Total: {total_profit_loss}\n"
   f"Average Change: ${average:.2f}\n"
   f"Greatest Increase: {greatest_increase_month} ${greatest_increase_value}\n"
   f"Greatest Decrease: {greatest_decrease_month} ${greatest_decrease_value}\n"
)


# In[ ]:


print(output)


# In[ ]:


with open("Bank_results.txt", "w") as filewriter:
    filewriter.write(output)


# In[ ]:





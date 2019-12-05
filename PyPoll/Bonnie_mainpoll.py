#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
import csv


# In[2]:


# Set variables
total_votes = 0
list_of_names = [] #empty list
percent_list = []
winner = 0

# use dictionaries
candidate_count = {} #empty dictionary


# In[3]:


poll_file = open("election_data.csv", "r")


# In[4]:


# print(poll_file)


# In[5]:


poll_result = csv.reader(poll_file, delimiter= ",")


# In[6]:


csv_header = next(poll_result)


# In[7]:


#loop through to count total number of votes
for row in poll_result:
    total_votes = total_votes + 1
    
    candidate_name = row[2] 
    if candidate_name not in list_of_names:
        list_of_names.append(candidate_name)
        candidate_count[candidate_name] = 0
    candidate_count[candidate_name] = candidate_count[candidate_name] +1 
    
    #individual_votes = candidate_count[candidate_name]


# In[8]:


print(list_of_names)
print(total_votes)
print(candidate_count)


# In[9]:


for i in candidate_count:
    print(i, candidate_count[i])


# In[10]:


max_votes = ["", 0]

for key, value in candidate_count.items():
    #print(key)
    #print(value)
    if value > max_votes[1]:
        max_votes[1] = value
        max_votes[0] = key
        
print(max_votes)

winner = max_votes[0]
print(winner)


# In[11]:


for candidate_name in candidate_count:
        percent_votes = candidate_count[candidate_name]/total_votes
        percent_list.append(percent_votes)


# In[12]:


def candidate_percentages():
    output = ""
    for index in range(0,4):
        output += f"{list_of_names[index]}: {percent_list[index]:.2%} ({candidate_count[list_of_names[index]]})\n"
    return output


# In[13]:


print(candidate_percentages())


# In[14]:


poll_results = candidate_percentages()


# In[15]:


final_poll_results = (
f"\nElection Results\n"
f"{poll_results}\n"
f"Winner: {winner}\n"
)


# In[16]:


# print(poll_results)
print(final_poll_results)


# In[17]:


#initiate csv writer


# In[18]:


# write how many votes each candidate received
with open("Final_poll_results.txt", "w") as filewriter:
    filewriter.write(final_poll_results)


# In[ ]:





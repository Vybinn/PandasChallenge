#!/usr/bin/env python
# coding: utf-8

# ### Observations from the data
# * 1. Male players are signficantly more numerous than female players, with more than five times the number of players.  This can inform future advertising and promotional efforts, advertising in bars, live streams of sporting events, and male-centric programming.
# * 2. Roughly 66% of the players are between the ages of 16-25, which suggests a marketing campaign targeted toward late high school students, college students and young professionals could be effective. 
# * 3. For the most part, the most popular items are also on the higher end of their item cost scale, and are among the most profitable.  This suggests that the company is doing a good job to incentivize or create demand for their more expensive items.  

# In[49]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
game_file = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
game_data_df = pd.read_csv(game_file)
game_data_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[50]:


game_data_df.columns


# In[51]:


player_count = len(game_data_df["SN"].unique())
player_count


# In[52]:


player_count_df = pd.DataFrame({"Total Players" : [player_count]})
player_count_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[53]:


#Determine the number of unique items for purchase
num_unique_items = len(game_data_df["Item ID"].unique())
num_unique_items


# In[54]:


#Determine average purchase price
average_purchase_price = game_data_df["Price"].mean()
average_purchase_price = round((average_purchase_price), 2)
average_purchase_price


# In[55]:


#Determine number of purchases
number_of_purchases = len(game_data_df["Purchase ID"].unique())
number_of_purchases


# In[56]:


#Determine total revenue
total_revenue = game_data_df["Price"].sum()
total_revenue


# In[57]:


sales_table = pd.DataFrame({"Number of Unique Items": [num_unique_items], "Average Price": average_purchase_price, 
                            "Number of Purchases" :number_of_purchases, "Total Revenue": total_revenue})
sales_table


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[58]:


#Determine number of unique players of each gender
gender_ids = game_data_df[["SN", "Gender"]]
gender_ids.head()
gender_ids_uni = gender_ids.drop_duplicates(["SN"])
unique_gender_count = gender_ids_uni["Gender"].value_counts()
unique_gender_count


# In[59]:


#Determine % of overall players by gender
male_players = 484
female_players = 81
other_players = 11
male_players_pct = (male_players/576) *100
female_players_pct = (female_players/576) *100
other_players_pct = (other_players/576) *100
male_players_pct = round(male_players_pct)
female_players_pct = round(female_players_pct)
other_players_pct = round(other_players_pct)
print(male_players_pct)
print(female_players_pct)
print(other_players_pct)


# In[60]:


#Create data frame of players by gender 
players_by_gender_df = pd.DataFrame({"Gender": ["Male", "Female", "Other / Undisclosed"], 
                                    "Total Number": [str(male_players), str(female_players), str(other_players)],
                                    "Percent of Players" : [male_players_pct, female_players_pct, other_players_pct]
}
)


players_by_gender_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[61]:


#Group purchase data by gender, and set up unique users per genre
purchases_by_gender = game_data_df.groupby("Gender")
unique_gender_values = purchases_by_gender["SN"].nunique()


# In[62]:


#Determine number of purchases by gender
purchase_count_gnd = purchases_by_gender["Purchase ID"].count()


# In[63]:


#Determine average purchase price by gender
avg_purchprice_gnd = purchases_by_gender["Price"].mean()
avg_purchprice_gnd = round((avg_purchprice_gnd),2)


# In[64]:


#Determine total purchase value by gender
tot_purchprice_gnd = purchases_by_gender["Price"].sum()


# In[65]:


#Determine average purchase total per person by gender
apt_pp_gnd = tot_purchprice_gnd / unique_gender_values
apt_pp_gnd = round((apt_pp_gnd),2)


# In[66]:


# Create summary data frame for purchases by gender  
purchase_summary_bygender = pd.DataFrame({"Purchase Count": purchase_count_gnd,
                                    "Total Purchase Value" : tot_purchprice_gnd,
                                    "Average Purchase Price": avg_purchprice_gnd,
                                    "Avg Total Purchase per Person": apt_pp_gnd})
purchase_summary_bygender


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[67]:


#Establish age bins
age_bins = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
group_names = ["5-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45", "46+"]


# In[68]:


# Assign all players to an age bin 
game_data_df["Player Age Group"] = pd.cut(game_data_df["Age"],age_bins, labels=group_names)
game_data_df


# In[69]:


#Reconfigure data by age group
age_groups = game_data_df.groupby("Player Age Group")


# In[70]:


#Determine total players by age category
total_byagegroup = age_groups["SN"].nunique()


# In[71]:


#Determine percentage of players by age category 
percentage_byage = (total_byagegroup/player_count) * 100
percentage_byage = round((percentage_byage), 2)


# In[72]:


#Create data frame for age demographics summary
age_demo_summary = pd.DataFrame({"Total Count": total_byagegroup, "Percentage of Players": percentage_byage})
age_demo_summary


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[73]:


#Bin purchases by age group
purchases_byage = age_groups["Purchase ID"].count()


# In[74]:


#Determine average purchase price by age group 
avg_purchase_price_byage = age_groups["Price"].mean()
avg_purchase_price_byage = round((avg_purchase_price_byage), 2)


# In[75]:


#Determine total purchase value by age group
total_purchase_value_byage = age_groups["Price"].sum()


# In[76]:


#Average total per person by age group
avg_totalpp_byage = total_revenue/total_byagegroup
avg_totalpp_byage = round((avg_totalpp_byage), 2)


# In[77]:


#DataFrame for purchases by age group
purchases_df_byagegroup = pd.DataFrame({"Purchase Count": purchases_byage,
                                       "Average Purchase Price": avg_purchase_price_byage,
                                       "Total Purchase Value": total_purchase_value_byage,
                                       "Average Total Purchase Per Person": avg_totalpp_byage})
purchases_df_byagegroup


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[78]:


#Group total purchases by Screen Names
totals_bysn = game_data_df.groupby("SN")


# In[79]:


#Determine total purchases by Screen Names 
total_purchcnt_bysn = totals_bysn["Purchase ID"].count()


# In[80]:


#Determine average purchase price by Screen Name 
avg_purch_bysn = totals_bysn["Price"].mean()
avg_purch_bysn = round((avg_purch_bysn), 2)


# In[81]:


#Determine purchase total value by Screen Name 
total_purchval_bysn = totals_bysn["Price"].sum()


# In[82]:


#Create Data Frame for Screen Name summary
sn_summary_df = pd.DataFrame({"Purchase Count": total_purchcnt_bysn,
                             "Average Purchase Price": avg_purch_bysn,
                             "Total Purchase Value": total_purchval_bysn})


# In[83]:


# Sort descending to list top five spenders by Screen Name  
top_spenders_bysn = sn_summary_df.sort_values(["Total Purchase Value"], ascending=False).head()
top_spenders_bysn


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[84]:


#Retrieve Item ID, Item Name and Item Price columns 
item_info = game_data_df[["Item ID", "Item Name", "Price"]]


# In[85]:


#Group by Item ID and Item Name
popular_items = item_info.groupby(["Item ID", "Item Name"])


# In[86]:


#Determine purchase count by item
count_byitem = popular_items["Price"].count()


# In[87]:


#Determine total value of items
totval_byitem = (popular_items["Price"].sum())


# In[88]:


#Determine individual item price 
price_byitem = (totval_byitem / count_byitem) 


# In[89]:


#Create summary data frame for most popular items
popular_summary = pd.DataFrame({"Purchase Count": count_byitem,
                               "Item Price": price_byitem,
                                "Total Value of Item": totval_byitem,
                                })
most_popular_summary = popular_summary.sort_values(["Purchase Count"], ascending=False).head()
most_popular_summary


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[90]:


#Sort Most Popular Item Data Frame by purchase value in descending order 
most_profitable_byvalue = most_popular_summary.sort_values(["Total Value of Item"],
                                                   ascending=False).head()
most_profitable_byvalue


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the dependencies.
import pandas as pd
import os
from datetime import date
import requests
import csv


# In[2]:


#basic call for standings for a given season
# "https://statsapi.web.nhl.com/api/v1/standings"
#indicates what season we want. format year start year end
season=""
# exanded variable required for win loss tally
# &expand=standings.record

query_url= f"https://statsapi.web.nhl.com/api/v1/standings?expand=standings.record{season}"
# query_url


# In[3]:


#request data from API
hockey_response = requests.get(query_url)
# hockey_response


# In[4]:


hockey_json = hockey_response.json()
date_ran = date.today()
# print(date_ran)
# pprint(hockey_json)


# In[5]:


# #finding variables in hockey_json
# #name of team
# team_name = hockey_json['records'][0]['teamRecords'][0]['team']['name']

# #name of Division
# team_division = hockey_json['records'][0]['division']['name']

# #name of Conference
# team_conference = hockey_json['records'][0]['conference']['name']

# #name of league
# team_league = hockey_json['records'][0]['league']['name']

# #number of games played "gp"
# team_gp = hockey_json['records'][0]['teamRecords'][0]['gamesPlayed']

# #number of wins "W"
# team_W = hockey_json['records'][0]['teamRecords'][0]['leagueRecord']['wins']

# #number of losses "L"
# team_L = hockey_json['records'][0]['teamRecords'][0]['leagueRecord']['losses']

# #number of overtime losses "QTL"
# team_QTL = hockey_json['records'][0]['teamRecords'][0]['leagueRecord']['ot']

# #number of points overall "Pts"
# team_Pts = hockey_json['records'][0]['teamRecords'][0]['points']

# #number of total goals scored by the team "GF"
# team_GF = hockey_json['records'][0]['teamRecords'][0]['goalsScored']

# #number of total goals allowed by the team "GA"
# team_GA = hockey_json['records'][0]['teamRecords'][0]['goalsAgainst']

# #goal differential "diff"
# team_diff = team_GF - team_GA

# #win loss in last ten games "L10"
# team_L10_w = hockey_json['records'][0]['teamRecords'][0]['records']['overallRecords'][3]['wins']
# team_L10_l = hockey_json['records'][0]['teamRecords'][0]['records']['overallRecords'][3]['losses']
# team_L10_o = hockey_json['records'][0]['teamRecords'][0]['records']['overallRecords'][3]['ot']
# team_L10 = f"'{team_L10_w}-{team_L10_l}-{team_L10_o}"

# #game streak "strk"
# team_strk = hockey_json['records'][0]['teamRecords'][0]['streak']['streakCode']


# #empty dataframe
# test_df = pd.DataFrame(columns=('Team','Conference','Division','League','GP','W','L','QTL','Pts','GF','GA','Diff','L10','Strk'))

# test = {'Team' : team_name,
#            'Division':team_division,
#            'Conference':team_conference,
#            'League':team_league,
#            'GP': team_gp,
#            'W': team_W,
#            'L': team_L,
#            'QTL': team_QTL,
#            'Pts': team_Pts,
#            'GF': team_GF,
#            'GA': team_GA,
#            'Diff': team_diff,
#            'L10': team_L10,
#            'Strk': team_strk}

# test_df = test_df.append(test,ignore_index=True)

# test_df


# In[6]:


# building loops to get info on all teams
x=0
y=0

current_stat_df=pd.DataFrame(columns=('Team','Conference','Division','GP','W','L','QTL','Pts','GF','GA','Diff','L10','Strk'))

x_max = len(hockey_json['records'])

while x < x_max:
    y = 0  
    y_max = len(hockey_json['records'][x]['teamRecords'])
    while y < y_max:
        team_name = hockey_json['records'][x]['teamRecords'][y]['team']['name']
        team_division = hockey_json['records'][x]['division']['name']
        team_conference = hockey_json['records'][x]['conference']['name']
        team_gp = hockey_json['records'][x]['teamRecords'][y]['gamesPlayed']
        team_W = hockey_json['records'][x]['teamRecords'][y]['leagueRecord']['wins']
        team_L = hockey_json['records'][x]['teamRecords'][y]['leagueRecord']['losses']
        team_QTL = hockey_json['records'][x]['teamRecords'][y]['leagueRecord']['ot']
        team_Pts = hockey_json['records'][x]['teamRecords'][y]['points']
        team_GF = hockey_json['records'][x]['teamRecords'][y]['goalsScored']
        team_GA = hockey_json['records'][x]['teamRecords'][y]['goalsAgainst']
        team_diff = team_GF - team_GA
        team_L10_w = hockey_json['records'][x]['teamRecords'][y]['records']['overallRecords'][3]['wins']
        team_L10_l = hockey_json['records'][x]['teamRecords'][y]['records']['overallRecords'][3]['losses']
        team_L10_o = hockey_json['records'][x]['teamRecords'][y]['records']['overallRecords'][3]['ot']
        team_L10 = f"'{team_L10_w}-{team_L10_l}-{team_L10_o}"
        team_strk = hockey_json['records'][x]['teamRecords'][y]['streak']['streakCode']
        
        
        team = {'Team' : team_name,
           'Division':team_division,
           'Conference':team_conference,
           'GP': team_gp,
           'W': team_W,
           'L': team_L,
           'QTL': team_QTL,
           'Pts': team_Pts,
           'GF': team_GF,
           'GA': team_GA,
           'Diff': team_diff,
           'L10': team_L10,
           'Strk': team_strk}
        
        current_stat_df = current_stat_df.append(team,ignore_index=True)
        y = y + 1
    x = x + 1

# current_stat_df


# In[7]:


#create .csv
title = f'hockey_stats_{date_ran}'
# Create the output file (CSV).
output_data_file = os.path.join("output",f"{title}.csv")
# Export the City_Data into a CSV.
current_stat_df.to_csv(output_data_file, index_label="Index_ID")


# In[ ]:





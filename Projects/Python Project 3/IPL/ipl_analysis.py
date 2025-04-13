# IPL Data Analysis with Pandas, NumPy, and Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/Abhijith911/Abhijith911/refs/heads/main/Projects/Python%20Project%203/IPL/matches.csv"  
matches = pd.read_csv(url)

print("First few rows of the dataset:")
print(matches.head())
print("\nDataset Shape:", matches.shape)
print("\nColumns:", matches.columns)

top_teams = matches['team1'].value_counts().head(10)
print("\nTop 10 Teams with Most Matches as team1:")
print(top_teams)

team_shortforms = {
    "Mumbai Indians": "MI",
    "Chennai Super Kings": "CSK",
    "Royal Challengers Bangalore": "RCB",
    "Kolkata Knight Riders": "KKR",
    "Sunrisers Hyderabad": "SRH",
    "Delhi Capitals": "DC",
    "Kings XI Punjab": "KXIP",
    "Rajasthan Royals": "RR",
    "Gujarat Lions": "GL",
    "Rising Pune Supergiant": "RPS"
}

top_teams.index = top_teams.index.map(lambda x: team_shortforms.get(x, x))

plt.figure(figsize=(10, 6))
top_teams.plot(kind='bar', color='skyblue')
plt.title("Top 10 Teams with Most Matches (Team1)")
plt.xlabel("Team")
plt.ylabel("Number of Matches")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
top_players = matches['player_of_match'].value_counts().head(10)
top_players.plot(kind='bar', color='orange')
plt.title("Top 10 Players with Most Player of the Match Awards")
plt.xlabel("Player")
plt.ylabel("Awards")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
matches_per_season = matches['season'].value_counts().sort_index()
matches_per_season.plot(kind='line', marker='o', color='green')
plt.title("Number of Matches per IPL Season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.grid(True)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

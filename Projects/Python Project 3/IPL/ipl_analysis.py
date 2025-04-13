import pandas as pd

url = "https://raw.githubusercontent.com/Abhijith911/Abhijith911/refs/heads/main/Projects/Python%20Project%203/IPL/matches.csv"  
matches = pd.read_csv(url)

print("First few rows of the dataset:")
print(matches.head())

print("\nDataset Shape:", matches.shape)
print("Columns:", matches.columns)

top_teams = matches['team1'].value_counts().head(10)
print("\nTop 10 Teams with Most Wins (team1):")
print(top_teams)

missing_values = matches.isnull().sum()


print("\nMissing Values in the Dataset:")
print(missing_values)

average_score_team1 = matches.groupby('team1')['team1_runs'].mean().sort_values(ascending=False)
average_score_team2 = matches.groupby('team2')['team2_runs'].mean().sort_values(ascending=False)

print("\nAverage Score by Team 1:")
print(average_score_team1.head(10))

print("\nAverage Score by Team 2:")
print(average_score_team2.head(10))

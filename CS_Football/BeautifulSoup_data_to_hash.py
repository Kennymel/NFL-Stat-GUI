import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# URL
url = "https://www.pro-football-reference.com/teams/oti/2024.htm#rushing_and_receiving"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.content, "html.parser")

# Locate table
table = soup.find("table", {"id": "rushing_and_receiving"})

# header
header_row = table.find("thead").find_all("tr")[-1]
headers = [th.text.strip() for th in header_row.find_all("th")]

# data rows
rows = []
for row in table.find("tbody").find_all("tr"):
    if row.get("class") and "thead" in row.get("class"):  
        continue
    cols = [col.text.strip() for col in row.find_all(["th", "td"])]
    if cols: 
        rows.append(cols)

# row -> data frame
df = pd.DataFrame(rows, columns=headers)


df = df[df["Player"].notna()]


df = df.loc[:, ~df.columns.duplicated()]

# Convert to hash table with player names as keys
player_data = {}
for _, row in df.iterrows():
    player_name = row["Player"].strip()  # Player name key
    player_info = {col: row[col] for col in df.columns if col != "Player"}  
    player_data[player_name] = player_info

# hash table into JSON file
output_file = "z_titans_2024_rushing_and_receiving_data.json"
with open(output_file, "w") as f:
    json.dump(player_data, f, indent=4)

print(f"Hash table saved to {output_file}")

'''
Defensive graph based on most recent match up
'''
import networkx as nx
import json
import zipfile

# Path to the zip file containing player stats
zip_file_path = r"C:\Users\Kenny\.vscode\CS_Football\z_all_2024_rushing_and_receiving_data.zip"

# Initialize the defensive graph
defensive_graph = nx.DiGraph()

# List of NFL teams
teams = [
    "Titans", "Colts", "Jaguars", "Texans", "Chiefs", "Ravens", "Bills", "Dolphins",
    "Bengals", "Broncos", "Patriots", "Browns", "Chargers", "Jets", "Raiders", "Steelers"
]

# Add teams as nodes with default defensive stats
for team in teams:
    defensive_graph.add_node(team, defense_stats={
        "rush_yards_allowed": 0,
        "receive_yards_allowed": 0,
        "rush_tds_allowed": 0,
        "receive_tds_allowed": 0
    })

# Function to update team defensive stats
def update_team_stats(team_name, rush_yards, receive_yards, rush_tds, receive_tds):
    """Update defensive stats for a team."""
    if team_name in defensive_graph:
        defensive_graph.nodes[team_name]["defense_stats"] = {
            "rush_yards_allowed": rush_yards,
            "receive_yards_allowed": receive_yards,
            "rush_tds_allowed": rush_tds,
            "receive_tds_allowed": receive_tds
        }
    else:
        print(f"Team {team_name} not found in the graph.")

# Update example team defensive stats
update_team_stats("Bills", 121.9, 199.7, 0.77, 1.38)
update_team_stats("Dolphins", 107.5, 203.9, 0.923,1.08 )
update_team_stats("Patriots", 124.7, 215.5, 0.85, 1.69)
update_team_stats("Jets", 126.2, 220.5, 1.38, 0.85)
update_team_stats("Bengals", 128.2, 241, 1.23, 1.85)
update_team_stats("Ravens", 82.7, 264.9, 0.85, 1.77)
update_team_stats("Steelers", 90.5, 220.5, 0.923, 1.08)
update_team_stats("Browns", 128.6, 221, 1.38, 1.38)
update_team_stats("Texans", 109.7, 198.8, 0.54, 2)
update_team_stats("Colts", 147, 232.4, 1.08, 1.31)
update_team_stats("Jaguars", 133.2, 273.3, 1.15, 1.85)
update_team_stats("Titans", 120.1, 229.8, 1.15, 1.54)
update_team_stats("Chiefs", 87.8, 224.1, 0.77, 1.38)
update_team_stats("Raiders", 114.8, 212.9, 0.923, 1.85)
update_team_stats("Chargers", 119.4, 206.4, 0.46, 1.15)
update_team_stats("Broncos", 94.7, 221, 0.46, 1.31)


# Function to load player stats from the zip file
def load_player_stats(zip_file_path):
    """Load player stats from JSON files within a zip archive."""
    player_stats_hash_table = {}
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            # Extract all JSON files
            files = [f for f in zip_file.namelist() if f.endswith('.json')]
            for file in files:
                with zip_file.open(file) as json_file:
                    data = json.load(json_file)
                    # Update the hash table with player data
                    player_stats_hash_table.update(data)
    except Exception as e:
        print(f"Error loading player stats: {e}")
    return player_stats_hash_table

player_stats_hash_table = load_player_stats(zip_file_path)

def fetch_team_defense_stats(team_name):
    """Fetch defensive stats for a specific team."""
    if team_name in defensive_graph:
        return defensive_graph.nodes[team_name]["defense_stats"]
    else:
        print(f"Team {team_name} not found.")
        return None

def predict_performance(player_name, team_name):
    """Predict a player's performance against a team's defense."""
    if player_name not in player_stats_hash_table:
        return f"Player {player_name} not found in hash table."
    
    player_stats = player_stats_hash_table[player_name]
    
    team_defense_stats = fetch_team_defense_stats(team_name)
    if not team_defense_stats:
        return f"Team {team_name} not found in graph."

    # Calculate performance comparison
    yards_exp = (int(player_stats["YScm"])/13 + team_defense_stats["rush_yards_allowed"] + team_defense_stats["rush_yards_allowed"])/3
    tds_exp = (int(player_stats["RRTD"])/13 + (team_defense_stats["rush_tds_allowed"] + team_defense_stats["receive_tds_allowed"])/3
    )


    # Output specific prediction numbers
    return {
        "player_name": player_name,
        "team_name": team_name,
        "Yards Expected": yards_exp,
        "Touchdowns Expected": tds_exp,
    }

# Example predictions
player_name_1 = "Derrick Henry"  # Replace with a valid player name from your JSON files
team_name_1 = "Colts"

player_name_2 = "Jonathan Taylor"  # Replace with a valid player name from your JSON files
team_name_2 = "Titans"

prediction_1 = predict_performance(player_name_1, team_name_1)
prediction_2 = predict_performance(player_name_2, team_name_2)

# Output the predictions
print("Prediction 1:", prediction_1)
print("Prediction 2:", prediction_2)

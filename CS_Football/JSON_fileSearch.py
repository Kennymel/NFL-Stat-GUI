import json
import os

# Function to load player data from multiple JSON files
def load_player_data_from_files(file_paths):
    all_player_data = {}
    for file_path in file_paths:
        try:
            with open(file_path, "r") as f:
                player_data = json.load(f)
                all_player_data.update(player_data)  # Merge player data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error reading JSON from file: {file_path}")
    return all_player_data

# Function to search for a player by name
def search_player(player_name, player_data):
    # Check if the player is in the hash table
    player_info = player_data.get(player_name)
    return player_info

# List of JSON files to search
json_files = [
    "z_ravens_2024_rushing_and_receiving_data.json",  
    "z_steelers_2024_rushing_and_receiving_data.json",
    "z_bengals_2024_rushing_and_receiving_data.json", 
    "z_browns_2024_rushing_and_receiving_data.json",
    "z_bills_2024_rushing_and_receiving_data.json",
    "z_broncos_2024_rushing_and_receiving_data.json",
    "z_chargers_2024_rushing_and_receiving_data.json",
    "z_chiefs_2024_rushing_and_receiving_data.json",
    "z_colts_2024_rushing_and_receiving_data.json",
    "z_dolphins_2024_rushing_and_receiving_data.json",
    "z_jaguars_2024_rushing_and_receiving_data.json",
    "z_jets_2024_rushing_and_receiving_data.json",
    "z_patriots_2024_rushing_and_receiving_data.json",
    "z_raiders_2024_rushing_and_receiving_data.json",
    "z_texans_2024_rushing_and_receiving_data.json",
    "z_titans_2024_rushing_and_receiving_data.json"
]

# Load player data from all specified JSON files
player_data = load_player_data_from_files(json_files)

# Main program loop for user input
while True:
    # Prompt the user for the player's name
    player_name = input("Enter the player's name (or type 'exit' to quit): ").strip()
    
    # Check if the user wants to exit the program
    if player_name.lower() == "exit":
        print("Exiting program.")
        break
    
    # Search for the player and get their stats
    player_info = search_player(player_name, player_data)
    
    if player_info:
        # If player is found, display their stats
        print(f"\nStats for {player_name}:")
        for stat, value in player_info.items():
            print(f"{stat}: {value}")
        print()  # Add an empty line after displaying stats
    else:
        # If player is not found, display a message
        print(f"Player '{player_name}' not found.\n")


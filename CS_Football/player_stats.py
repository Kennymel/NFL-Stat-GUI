'''
Very hard to scrape player data off the web so I will incorporate a limited amount of players 
Storing each players data in a hash table 
'''
from prettytable import PrettyTable
# Create a hash table (dictionary) for NFL players
class PlayerData:
    ravens_offense = {
        "Lamar Jackson": {"team": "Ravens", "position": "QB","passing yards": 3290  ,"GP" : 13, "passing touchdowns": 29, "INT" : 3},
        "Derrick Henry": {"team": "Ravens", "position": "RB","rushing yards": 1407 , "GP" : 13, "rushing touchdowns": 13, "carries": 240},
        "Justice Hill": {"team": "Ravens", "position": "RB","rushing yards": 191 , "GP" : 13, "rushing touchdowns": 1, "carries": 43},
        "Zay Flowers": {"team": "Ravens", "position": "WR", "receiving yards": 863 , "GP" : 13, "receiving touchdowns": 4, "receptions": 60},
        "Rashod Bateman": {"team": "Ravens", "position": "WR", "receiving yards": 574 , "GP" : 13, "receiving touchdowns": 5, "receptions": 35},
        "Nelson Agholor": {"team": "Ravens", "position": "WR", "receiving yards": 205 , "GP" : 13, "receiving touchdowns": 2, "receptions": 13},
        "Mark Andrews": {"team": "Ravens", "position": "TE", "receiving yards": 490 , "GP" : 13, "receiving touchdowns": 7, "receptions": 43},
        "Isaiah Likely": {"team": "Ravens", "position": "TE", "receiving yards": 384 , "GP" : 12, "receiving touchdowns": 4, "receptions": 33},
    }

    ravense_defense = {
        "Ravens" : {"Passing Yards Allowed per game": 264.92, "Rushing yards allowed per game": 82.69, "touchdowns allowed per game": 2.61 }
    }

    steelers_offense = {
        "Russell Wilson": {"team": "Steelers", "position": "QB","passing yards": 1626  ,"GP" : 6, "passing touchdowns": 10, "INT" : 3},
        "Justin Fields": {"team": "Steelers", "position": "QB","passing yards": 1106  ,"GP" : 9, "passing touchdowns": 5, "INT" : 1},
        "Najee Harris": {"team": "Steelers", "position": "RB","rushing yards": 824 , "GP" : 12, "rushing touchdowns": 4, "carries": 207},
        "Jaylen Warren": {"team": "Steelers", "position": "RB","rushing yards": 312 , "GP" : 10, "rushing touchdowns": 1, "carries": 78},
        "George Pickens": {"team": "Steelers", "position": "WR", "receiving yards": 850 , "GP" : 12, "receiving touchdowns": 3, "receptions": 55},
        "Calvin Austin": {"team": "Steelers", "position": "WR", "receiving yards": 383 , "GP" : 12, "receiving touchdowns": 4, "receptions": 22},
        "Van Jefferson": {"team": "Steelers", "position": "WR", "receiving yards": 221 , "GP" : 12, "receiving touchdowns": 1, "receptions": 17},
        "Pat Freiermuth": {"team": "Steelers", "position": "TE", "receiving yards": 422 , "GP" : 12, "receiving touchdowns": 4, "receptions": 41},
        "Darnell Washington": {"team": "Steelers", "position": "TE", "receiving yards": 192 , "GP" : 12, "receiving touchdowns": 1, "receptions": 18},
    }


# Function to get the stats based on position
def get_position_stats(position, player_stats):
    if position == "QB":
        return ["passing yards", "passing touchdowns", "INT"]
    elif position == "RB":
        return ["rushing yards", "rushing touchdowns", "carries"]
    elif position == "WR" or position == "TE":
        return ["receiving yards", "receiving touchdowns", "receptions"]
    else:
        return []

# Function to print player stats based on their name
def print_player_stats():
    player_name = input("Enter an AFC North player (case sensitive): ")

    # Merge data from both teams
    players_data = {**PlayerData.ravens_offense, **PlayerData.steelers_offense}

    if player_name in players_data:
        # Get player stats
        player_stats = players_data[player_name]
        position = player_stats["position"]

        # Create a table to display player data
        table = PrettyTable()
        
        # Set the field names based on the player's position
        field_names = ["Name", "Team", "Position"] + get_position_stats(position, player_stats)
        table.field_names = field_names

        # Add player data to the table
        row = [player_name, player_stats["team"], player_stats["position"]]
        
        # Add the relevant stats based on the player's position
        for stat in get_position_stats(position, player_stats):
            row.append(player_stats.get(stat, "N/A"))
        
        table.add_row(row)
        print(table)
    else:
        print(f"{player_name} not found in the database.")

# Call the function to display stats
print_player_stats()
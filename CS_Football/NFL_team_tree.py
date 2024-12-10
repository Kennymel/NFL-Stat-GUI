from player_vs_def_stat import defensive_graph

class TreeNode:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data  
        self.children = {}

    def add_child(self, child_name, data=None):
        if child_name not in self.children:
            self.children[child_name] = TreeNode(child_name, data)
        return self.children[child_name]

    def get_child(self, child_name):
        return self.children.get(child_name, None)

    def get_children_names(self):
        return list(self.children.keys())

nfl_tree = TreeNode("NFL")

# Define conferences and their teams
afc_teams = [
    "Titans", "Colts", "Jaguars", "Texans", "Chiefs", "Ravens", "Bills",
    "Dolphins", "Bengals", "Broncos", "Patriots", "Browns", "Chargers",
    "Jets", "Raiders", "Steelers"
]

nfc_teams = [
    # add rest of teams
]

# conference tree
afc_node = nfl_tree.add_child("AFC")
nfc_node = nfl_tree.add_child("NFC")

# fill up teams
for team in afc_teams:
    team_stats = defensive_graph.nodes[team]["defense_stats"]
    afc_node.add_child(team, team_stats)


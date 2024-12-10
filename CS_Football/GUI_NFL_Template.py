from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import json
import zipfile
import os
from player_vs_def_stat import predict_performance, load_player_stats

# pull hash table zip
zip_file_path = r"C:\Users\Kenny\.vscode\CS_Football\z_all_2024_rushing_and_receiving_data.zip"
player_stats_hash_table = load_player_stats(zip_file_path)

# stack for search history
search_history = []

def add_to_search_history(player_name, prediction):
    search_history.append((player_name, prediction))

def undo_last_search():
    if search_history:
        last_search = search_history.pop()
        player_name, prediction = last_search

        # show prev. results
        result = f"Player: {player_name}\n\n"
        for key, value in prediction.items():
            result += f"{key}: {value}\n"

        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)
        result_text.config(state="disabled")
    else:
        messagebox.showinfo("Undo", "No searches to undo.")

def on_search_button_click():
    player_name = entry.get()
    team_name = team_var.get()

    if not player_name.strip() or not team_name.strip():
        messagebox.showwarning("Input Error", "Please enter a player name and select a team")
        return

    if player_name not in player_stats_hash_table:
        messagebox.showinfo("Not Found", f"No data found for player: {player_name}")
        return

    try:
        prediction = predict_performance(player_name, team_name)
        player_stats = player_stats_hash_table[player_name]

        # Add to stack for history
        add_to_search_history(player_name, prediction)

        # Display for prediction
        prediction_result = f"Player: {player_name}\nOpponent: {team_name}\n\n"
        prediction_result += f"Predicted Yards: {prediction['Yards Expected']}\n"
        prediction_result += f"Predicted Touchdowns: {prediction['Touchdowns Expected']}\n"

        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, prediction_result)
        result_text.config(state="disabled")

        # Display player stats
        stats_result = f"Player: {player_name}\n\n"
        for stat, value in player_stats.items():
            stats_result += f"{stat}: {value}\n"

        player_stats_text.config(state="normal")
        player_stats_text.delete("1.0", tk.END)
        player_stats_text.insert(tk.END, stats_result)
        player_stats_text.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while predicting stats: {e}")

def clear_results():
    entry.delete(0, tk.END)
    team_var.set("")
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.config(state="disabled")
    player_stats_text.config(state="normal")
    player_stats_text.delete("1.0", tk.END)
    player_stats_text.config(state="disabled")

# GUI set up
root = tk.Tk()
root.title("AFC NFL Player Performance")
root.geometry("900x500")  
root.configure(bg="#d1b897")

# Search bar / buttons
frame = tk.Frame(root, bg="#d1b897")
frame.pack(pady=20)

# search label & room for inputs
search_label = tk.Label(frame, text="Enter AFC Player Name", font=("Arial", 14, "bold"), bg="#d1b897", fg="#003b2a")
search_label.grid(row=0, column=0, padx=10, sticky="w")

entry = tk.Entry(frame, font=("Arial", 12), width=30, bd=2, relief="solid")
entry.grid(row=0, column=1, padx=10, columnspan=2, sticky="ew")

# defensive team selection 
team_label = tk.Label(frame, text="Select Defense", font=("Arial", 14, "bold"), bg="#d1b897", fg="#003b2a")
team_label.grid(row=1, column=0, padx=10, sticky="w")

team_var = tk.StringVar()
teams = [
    "Titans", "Colts", "Jaguars", "Texans", "Chiefs", "Ravens", "Bills", "Dolphins",
    "Bengals", "Broncos", "Patriots", "Browns", "Chargers", "Jets", "Raiders", "Steelers"
]
team_menu = tk.OptionMenu(frame, team_var, *teams)
team_menu.grid(row=1, column=1, padx=10, columnspan=2, sticky="ew")

# Button display and command
search_button = tk.Button(frame, text="Search", font=("Arial", 12), command=on_search_button_click, bg="#006747", fg="white", relief="raised")
search_button.grid(row=2, column=0, padx=10, pady=10)

undo_button = tk.Button(frame, text="Undo", font=("Arial", 12), command=undo_last_search, bg="#f0ad4e", fg="white", relief="raised")
undo_button.grid(row=2, column=1, padx=10, pady=10)

clear_button = tk.Button(frame, text="Clear", font=("Arial", 12), command=clear_results, bg="#d9534f", fg="white", relief="raised")
clear_button.grid(row=2, column=2, padx=10, pady=10)

# final fram 
result_frame = tk.Frame(root, bg="#d1b897")
result_frame.pack(pady=20, fill="both", expand=True, side="left")

# text for printed results
scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text = tk.Text(result_frame, font=("Arial", 12), bg="#d1b897", fg="#003b2a", wrap="word", state="disabled", yscrollcommand=scrollbar.set, relief="solid")
result_text.pack(padx=10, pady=10, fill="both", expand=True)

scrollbar.config(command=result_text.yview)

# text for stats
player_stats_frame = tk.Frame(root, bg="#d1b897")
player_stats_frame.pack(fill="both", expand=True, side="right", padx=10)

player_stats_text = tk.Text(player_stats_frame, font=("Arial", 12), bg="#d1b897", fg="#003b2a", wrap="word", state="disabled", relief="solid")
player_stats_text.pack(padx=10, pady=10, fill="both", expand=True)



root.mainloop()
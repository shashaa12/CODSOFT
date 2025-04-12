import tkinter as tk
from tkinter import messagebox
import random

# Choices
choices = ["rock", "paper", "scissors"]

# Scores
player_score = 0
computer_score = 0
ties = 0

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def update_score(winner):
    global player_score, computer_score, ties
    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1
    else:
        ties += 1

    score_label.config(
        text=f"Scores\nYou: {player_score}  Computer: {computer_score}  Ties: {ties}"
    )

def play(player_choice):
    computer_choice = random.choice(choices)
    winner = get_winner(player_choice, computer_choice)

    if winner == "tie":
        result = "It's a tie!"
    elif winner == "player":
        result = "You win!"
    else:
        result = "Computer wins!"

    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    update_score(winner)

    # Ask if user wants to play again
    again = messagebox.askyesno("Play Again?", "Do you want to play another round?")
    if not again:
        window.destroy()

# GUI Setup
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("350x350")
window.resizable(False, False)

tk.Label(window, text="Choose your move:", font=('Arial', 14)).pack(pady=10)

# Button Frame
btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

# Result Display
computer_label = tk.Label(window, text="", font=('Arial', 12))
computer_label.pack(pady=10)

result_label = tk.Label(window, text="", font=('Arial', 14, 'bold'))
result_label.pack(pady=5)

# Score Display
score_label = tk.Label(window, text="Scores\nYou: 0  Computer: 0  Ties: 0", font=('Arial', 12), justify="center")
score_label.pack(pady=10)

# Run the app
window.mainloop()

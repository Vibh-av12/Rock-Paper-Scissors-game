import tkinter as tk
import random

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

choices = ["Rock", "Paper", "Scissors"]

def determine_winner(player_choice):
    computer_choice = random.choice(choices)
    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

def on_button_click(choice):
    determine_winner(choice)

rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click("Rock"))
rock_button.pack(side=tk.LEFT, padx=20, pady=20)

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click("Paper"))
paper_button.pack(side=tk.LEFT, padx=20, pady=20)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

result_label = tk.Label(root, text="")
result_label.pack(side=tk.BOTTOM, pady=20)

root.mainloop()

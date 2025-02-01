import tkinter as tk

class HowToPlay:
    def __init__(self, root):
        self.root = root
        self.root.title('How to Play Rock-Paper-Scissors')

        welcome_label = tk.Label(self.root, text="Welcome to the Rock-Paper-Scissors Showdown!\nLet's learn how to play the game.", font=('Helvetica', 14, 'bold'), pady=10)
        welcome_label.pack()

        self.show_instructions()

        close_button = tk.Button(self.root, text="Close", command=self.root.destroy, font=('Helvetica', 12), bg='lightblue')
        close_button.pack(pady=5)

    def show_instructions(self):
        instructions = (
            "1. Prepare for Battle: Launch the game by running the `Rock-Paper-Scissors game.py`\n"
            "2. Choose Your Move: Click on 'Rock', 'Paper', or 'Scissors' to make your move.\n"
            "3. Witness the Clash: See the computer's choice displayed on the screen.\n"
            "4. Declare the Victor: The game will show who won based on the rules:\n"
            "   - Rock 🪨 crushes Scissors ✂️\n"
            "   - Scissors ✂️ slices Paper 📜\n"
            "   - Paper 📜 covers Rock 🪨\n"
            "5. Keep the Action Going: "
        )

        instruction_label = tk.Label(self.root, text=instructions, font=('Helvetica', 12), justify='left', padx=20, pady=20)
        instruction_label.pack()

# Create the main window
root = tk.Tk()
app = HowToPlay(root)

# Run the GUI loop
root.mainloop()


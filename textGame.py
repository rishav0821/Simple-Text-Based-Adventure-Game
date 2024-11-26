import tkinter as tk
from tkinter import messagebox

class AdventureGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-Based Adventure Game")
        self.current_scene = "start"
        
        # Main frame for content
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Story Label
        self.story_label = tk.Label(self.frame, text="", wraplength=400, font=("Arial", 14))
        self.story_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons for choices
        self.choice1_button = tk.Button(self.frame, text="Choice 1", width=20, command=lambda: self.next_scene(1))
        self.choice1_button.grid(row=1, column=0, padx=10, pady=5)
        self.choice2_button = tk.Button(self.frame, text="Choice 2", width=20, command=lambda: self.next_scene(2))
        self.choice2_button.grid(row=1, column=1, padx=10, pady=5)

        # Start the game
        self.start_game()
    
    def start_game(self):
        self.update_scene(
            "Welcome to the Adventurous Game!\n\nYou find yourself in a dark forest. You have two choices:\n1. Follow the narrow path.\n2. Enter the mysterious cave.",
            "Follow the Narrow Path",
            "Enter the Mysterious Cave"
        )
        self.current_scene = "start"

    def narrow_path(self):
        self.update_scene(
            "You walk along the narrow path and find a small wooden house. Inside, a stranger offers you food and rest.\n\n1. Accept the offer.\n2. Politely refuse and continue your journey.",
            "Accept the Offer",
            "Refuse and Continue"
        )
        self.current_scene = "narrow_path"

    def mysterious_cave(self):
        self.update_scene(
            "You enter the cave and hear a growl. There are two items on the ground: a torch and a sword.\n\n1. Pick up the torch.\n2. Pick up the sword.",
            "Pick up the Torch",
            "Pick up the Sword"
        )
        self.current_scene = "mysterious_cave"

    def end_game(self, message, success=True):
        if success:
            messagebox.showinfo("Game Over", message)
        else:
            messagebox.showerror("Game Over", message)
        self.start_game()

    def next_scene(self, choice):
        if self.current_scene == "start":
            if choice == 1:
                self.narrow_path()
            elif choice == 2:
                self.mysterious_cave()
        elif self.current_scene == "narrow_path":
            if choice == 1:
                self.end_game("The stranger was kind. You regain strength and safely leave the forest. You win!")
            elif choice == 2:
                self.end_game("You feel tired and lost in the forest. Without rest, you collapse. Game over.", success=False)
        elif self.current_scene == "mysterious_cave":
            if choice == 1:
                self.end_game("You light the torch and scare the creature away. You find treasure hidden in the cave. You win!")
            elif choice == 2:
                self.end_game("You take the sword, but the creature is too strong. It attacks, and you lose. Game over.", success=False)

    def update_scene(self, story, choice1, choice2):
        self.story_label.config(text=story)
        self.choice1_button.config(text=choice1)
        self.choice2_button.config(text=choice2)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = AdventureGameGUI(root)
    root.mainloop()

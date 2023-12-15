from random import sample
import tkinter as tk
from tkinter import ttk
from main.chess import start_game

class main_window:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("Chess Launcher")
        self.main.grid_rowconfigure('all', weight = 1)
        self.main.grid_rowconfigure('all', weight = 1)
        self.main.iconbitmap('icon.ico')
        opponentlabel = ttk.Label(self.main, text = "Choose Opponent: ")
        self.box = ttk.Combobox(self.main,state = 'readonly', values = ["No Engine", "Engine: Beginner", "Engine: Intermediate", "Engine: Hard"])
        self.box.set("No Engine")
        labelside = ttk.Label(self.main, text = "Choose your side:")
        button1 = ttk.Button(self.main, text = "Play", command = self.game)
        self.sidebox = ttk.Combobox(self.main, state = 'readonly', values = ["White","Black","Random"])
        self.sidebox.set("Random")
        opponentlabel.grid(row = 0,column = 0)
        self.box.grid(row = 0, column = 1)
        labelside.grid(row = 1, column = 0)
        self.sidebox.grid(row = 1, column =1)
        button1.grid(row = 3,column = 0, columnspan = 2)
        self.main.tk.mainloop()

    def game(self, event = None):
        name = self.box.get()
        side = self.sidebox.get()
        if side == "Random":
            side = sample(["White","Black"],1)[0]
        self.main.withdraw()
        self.start = start_game(side.lower(), name)
        self.main.deiconify()

if __name__ == "__main__":
    root = main_window()    

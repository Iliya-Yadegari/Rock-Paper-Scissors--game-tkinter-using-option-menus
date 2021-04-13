from tkinter import *
from random import randint

def Prs(value):

    t = ["Rock", "Paper", "Scissors"]
    
    computer = t[randint(0,2)]
    
    player = False
    
    while player == False:
    
        player = value.get()  

        if player == computer:
            txt = "Tie!"
        elif player == "Rock":
            if computer == "Paper":
                txt = "You lose!", computer, "covers", player
            else:
                txt = "You win!", player, "smashes", computer
        elif player == "Paper":
            if computer == "Scissors":
                txt = "You lose!", computer, "cut", player
            else:
                txt = "You win!", player, "covers", computer
        elif player == "Scissors":
            if computer == "Rock":
                txt = "You lose...", computer, "smashes", player
            else:
                txt = "You win!", player, "cut", computer
        else:
            txt = "That's not a valid play. Check your spelling!"
    
        messagebox.showinfo('Result',txt)
    
    
    
        computer = t[randint(0,2)]
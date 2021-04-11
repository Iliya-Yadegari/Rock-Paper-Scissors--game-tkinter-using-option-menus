from tkinter import *
from random import randint

def Prs():

    t = ["Rock", "Paper", "Scissors"]
    
    computer = t[randint(0,2)]
    
    player = False
    
    while player == False:
    
        player = r.get()  

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


window = Tk()
window.title('Rock Paper Scissors Game')

r = StringVar()

optionLst = ['Rock','Paper','Scissors']

r.set(optionLst[0])

main_frm = LabelFrame(window)
option_label = Label(main_frm,text = 'Chosse your move ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
drop = OptionMenu(main_frm,r,*optionLst).grid(row = 0, column = 1, padx = 10, pady = 10)submit_btn = Button(main_frm,text = 'Submit',width = 20, height = 3,command = Prs).grid(row = 1, column = 0, padx = 10, pady = 10)

main_frm.grid(row = 0, column = 0, padx = 10, pady = 10)

window.mainloop()
from tkinter import *
import PrsOptModule as pom

window = Tk()
window.title('Rock Paper Scissors Game')

r = StringVar()

optionLst = ['Rock','Paper','Scissors']

r.set(optionLst[0])

main_frm = LabelFrame(window)
option_label = Label(main_frm,text = 'Chosse your move ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
drop = OptionMenu(main_frm,r,*optionLst).grid(row = 0, column = 1, padx = 10, pady = 10)
submit_btn = Button(main_frm,text = 'Submit',width = 20, height = 3,command = lambda: pom.Prs(r)).grid(row = 1, column = 0, padx = 10, pady = 10)

main_frm.grid(row = 0, column = 0, padx = 10, pady = 10)

window.mainloop()
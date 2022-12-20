#import statement
import tkinter as tk
from _tkinter import *
import random


#variables
player_score = 0
artificial_score = 0
gamecount = ""
selection_1  = "Rock"
selection_2  = "Paper"
selection_3  = "Scissors"




#functions
def artificial():

    global ai_value
    ai_select = random.randint(1,3)
    if ai_select  == 1:
        ai_value = selection_1
        pass
    elif ai_select == 2:
        ai_value = selection_2
        pass
    else:
        ai_value = selection_3

    print(ai_select)
    print(ai_value)
    pass

#create GUI
root = tk.Tk()


#set window size
root.geometry("500x600")

#title on the screen
title = tk.Label(root, text="Rock Paper Scissors", font=("Open sans", 20), fg="#265BAA")
title.grid(row=0, column=0, columnspan=2, pady=10,padx=100)

#paragraph
paragraph = tk.Label(root, text="With Artificial Intelligent", fg="#265BAA", font=("Helvetica", 10))
paragraph.grid(row=1, column=0, columnspan=2, padx=100)

#gameui
score_title = tk.Label(root, text="Score", fg="#265BAA", font=("Open sans", 16))
score_title.grid(row=2, column=0, padx=100, columnspan=2, pady=20)

#PLAYERS

#human
human = tk.Label(root, text="Human", font=("Opensans"))
human.grid(row=4, column=0, padx=100, pady=20, columnspan=1)
human_score = tk.Label(root, text=player_score, font=("Opensans"))
human_score.grid(row=3, column=0, padx=100)

hvalue = tk.Label(root, text="ai_value", font=("Opensans", 14))
hvalue.grid(row=5, column=0, padx=100, pady=20, columnspan=1)


#ai
ai = tk.Label(root, text="AI", font=("Opensans"))
ai.grid(row=4, column=1, padx=100, pady=20)
ai_score = tk.Label(root, text=artificial_score, font=("Opensans"))
ai_score.grid(row=3, column=1, padx=100)


startgame = tk.Label(root, text="START GAME", font=("Opensans"), fg="#265BAA",)
startgame.grid(row=5, column=0, padx=100, pady=20, columnspan=2)


#BUTTONS

rock = tk.Button(root, text="Rock", font=("Opensans", 16), bg="#265BAA", fg="white", border="0", width="10", command=artificial)
rock.grid(row=6, column=0,columnspan=2, pady=5)

paper = tk.Button(root, text="Paper", font=("Opensans", 16), bg="#265BAA", fg="white", border="0", width="10" )
paper.grid(row=7, column=0,columnspan=2, pady=5)

scissors = tk.Button(root, text="Scissors", font=("Opensans", 16), bg="#265BAA", fg="white", border="0", width="10")
scissors.grid(row=8, column=0, columnspan=2, pady=5)


restart = tk.Button(root, text="Restart", font=("Opensans", 16), bg="white", fg="#265BAA", border="2", borderwidth="4", width="10")
restart.grid(row=9, column=0, columnspan=2, pady=20)















root.mainloop()

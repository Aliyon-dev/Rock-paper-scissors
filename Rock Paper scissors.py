#import statement
import tkinter as tk
from _tkinter import *
import random



#create GUI
root = tk.Tk()


#set window size
root.geometry("500x600")


#variables
player_score = 0
artificial_score = 0
gamecount = ""
selection_1  = "Rock"
selection_2  = "Paper"
selection_3  = "Scissors"
hu_value = ""





#functions




#when the player chooses rock
def rock_func():
    hu_value = selection_1
    avalue.configure(text=hu_value)
    print(hu_value)
    pass

#when the player chooses paper
def paper_func():
    hu_value = selection_2
    print(hu_value)
    avalue.configure(text=hu_value)
    pass

#when the player chooses scisssors
def Scissors_func():
    hu_value = selection_3
    avalue.configure(text=hu_value)
    print(hu_value)
    pass


def artificial():

    global ai_value
    ai_select = random.randint(1,3)
    if ai_select  == 1:
        ai_value = selection_1
        hvalue.configure(text=ai_value)
        pass
    elif ai_select == 2:
        ai_value = selection_2
        hvalue.configure(text=ai_value)
        pass
    else:
        ai_value = selection_3
        hvalue.configure(text=ai_value)
        pass

    

    print(ai_select)
    print(ai_value)
    pass



#def chooseWinner():
#    global score
#    score = 0
#
#    if hu_value == "Rock" and ai_value == "Paper":
#        score = ai_score + 1
#        print(score)
#        pass
#
#    elif hu_value == selection_1 and ai_value == selection_3:
#        ai_score =+ 1
#        print(score)
#        pass
#
#    print(score)
#
#    pass






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


hvalue = tk.Label(root, text="", font=("Opensans", 14))
hvalue.grid(row=5, column=1, padx=100, pady=20, columnspan=1)

avalue = tk.Label(root, text="", font=("Opensans", 14))
avalue.grid(row=5, column=0, padx=100, pady=20, columnspan=1)


#ai
ai = tk.Label(root, text="AI", font=("Opensans"))
ai.grid(row=4, column=1, padx=100, pady=20)
ai_score = tk.Label(root, text=artificial_score, font=("Opensans"))
ai_score.grid(row=3, column=1, padx=100)


startgame = tk.Label(root, text="START GAME", font=("Opensans"), fg="#265BAA",)
startgame.grid(row=6, column=0, padx=100, pady=20, columnspan=2)


#BUTTONS

rock = tk.Button(root, text="Rock", font=("Opensans", 16), bg="#265BAA", fg="white", border="0", width="10", command=lambda:(artificial(), rock_func()))
rock.grid(row=7, column=0,columnspan=2, pady=5)

paper = tk.Button(root, text="Paper", font=("Opensans", 16), bg="#265BAA", fg="white", border="0", width="10", command=lambda:(artificial(), paper_func()) )
paper.grid(row=8, column=0,columnspan=2, pady=5)

scissors = tk.Button(root, text="Scissors", font=("Opensans", 16), bg="#265BAA", fg="white", border="0", width="10", command=lambda:(artificial(), Scissors_func()))
scissors.grid(row=9, column=0, columnspan=2, pady=5)


restart = tk.Button(root, text="Restart", font=("Opensans", 16), bg="white", fg="#265BAA", border="2", borderwidth="4", width="10")
restart.grid(row=10, column=0, columnspan=2, pady=20)














root.mainloop()

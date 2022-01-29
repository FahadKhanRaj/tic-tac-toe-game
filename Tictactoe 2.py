from tkinter import *
import random

def turn_change(row,column):
    global single_player
    if boxes[row][column]['text'] == "" and winner_or_not() is False:
        if single_player == players[0]:
            boxes[row][column]['text'] = single_player

            if winner_or_not() is False:
                single_player = players[1]
                opening_title.config(text=(players[1]+"'s turn"))

            elif winner_or_not() is True:
                opening_title.config(text=(players[0]+" won the game"))

            elif winner_or_not() == "No Winner":
                opening_title.config(text="No Winner")

        else:

            boxes[row][column]['text'] = single_player

            if winner_or_not() is False:
                single_player = players[0]
                opening_title.config(text=(players[0]+"'s turn"))

            elif winner_or_not() is True:
                opening_title.config(text=(players[1]+" won the game"))
 

            elif winner_or_not() == "No Winner":
                opening_title.config(text="No Winner")

def winner_or_not():

    for row in range(3):
        if boxes[row][0]['text'] == boxes[row][1]['text'] == boxes[row][2]['text'] != "":
            boxes[row][0].config(bg="red",fg="#D4FF00")
            boxes[row][1].config(bg="red",fg="#D4FF00")
            boxes[row][2].config(bg="red",fg="#D4FF00")
            
            return True

    for column in range(3):
        
        if boxes[0][column]['text'] == boxes[1][column]['text'] == boxes[2][column]['text'] != "":
            boxes[row][0].config(bg="red",fg="#D4FF00")
            boxes[row][1].config(bg="red",fg="#D4FF00")
            boxes[row][2].config(bg="red",fg="#D4FF00")

            return True

    if boxes[0][0]['text'] == boxes[1][1]['text'] == boxes[2][2]['text'] != "":
        boxes[0][0].config(bg="red",fg="#D4FF00")
        boxes[1][1].config(bg="red",fg="#D4FF00")
        boxes[2][2].config(bg="red",fg="#D4FF00")
        return True

    elif boxes[0][2]['text'] == boxes[1][1]['text'] == boxes[2][0]['text'] != "":
        boxes[0][2].config(bg="red",fg="#D4FF00")
        boxes[1][1].config(bg="red",fg="#D4FF00")
        boxes[2][0].config(bg="red",fg="#D4FF00")
        return True

    elif blank() is False:

        for row in range(3):
            for column in range(3):
                boxes[row][column].config(bg="#979697")
        return "No Winner"

    else:
        return False


def blank():
    space = 9
    for row in range(3):
        for column in range(3):
            if boxes[row][column]['text'] != "":
                space=space-1

    if space == 0:
        return False
    else:
        return True

def restart():

    global single_player

    single_player = random.choice(players)

    opening_title.config(text=single_player+" turn")

    for row in range(3):
        for column in range(3):
            boxes[row][column].config(text="",bg="#34FFFC")


window = Tk()
window.title("Game of Tic Tac Toe:")


players = ["X","O"]
single_player = random.choice(players)
boxes = [[0,0,0],
           [0,0,0],
           [0,0,0]]

opening_title = Label(text=single_player + " will start", font=('Lucida Calligraphy',30), bg="#B512C5")
opening_title.pack(side="top")


restart_button = Button(text="Restart Game", font=('Impact',30), bg="#B512C5", fg="white", relief=SUNKEN, command=restart)
restart_button.pack(side="bottom")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        boxes[row][column] = Button(frame, text="",font=('Lucida Calligraphy',30), width=4, height=2, bg="#34FFFC",
                                      command= lambda row=row, column=column: turn_change(row,column))
        boxes[row][column].grid(row=row,column=column)

window.mainloop()
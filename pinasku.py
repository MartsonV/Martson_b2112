from tkinter import *
from tkinter import messagebox
from random import randint


def isEnd():
    global field
    # Check if the puzzle is solved
    for i in range(15):
        if field[i]["text"] != str(i + 1):
            return False
    messagebox.showinfo("Congratulations", "You won!")
    return True


def findEmptyCell():
     global field
     for i in range(16):
             if field[i]["text"]=="":
                return i


def keyPress(e):
    pos = findEmptyCell()
    if e.keycode == 38:  # Up ==38
        if pos<12:
            field[pos]["text"], field[pos + 4]["text"] = field[pos + 4]["text"], field[pos]["text"]
    if e.keycode == 37:  # Left ==37
        if (pos + 1) % 4 != 0:
            field[pos]["text"], field[pos + 1]["text"] = field[pos + 1]["text"], field[pos]["text"]
    if e.keycode == 40:  # Down ==40
        if pos>3:
            field[pos]["text"], field[pos - 4]["text"] = field[pos - 4]["text"], field[pos]["text"]
    if e.keycode == 39:  # Right ==39
        if pos % 4 != 3:
            field[pos]["text"], field[pos - 1]["text"] = field[pos - 1]["text"], field[pos]["text"]
    isEnd()



def setField():
    global field
    n = 0
    for i in range(4):
        for j in range(4):
            field.append(Label(form, width=6, height=3, font="Arial 20 bold", borderwidth=1, relief="solid"))
            field[n].grid(row=i, column=j)
            n += 1

    k = 1
    while k < 16:
        a = randint(0, 15)
        if field[a]["text"] == "":
            field[a]["text"] = str(k)
            k += 1


form = Tk()
form.title("Game")
form.resizable(False, False)

field = []
setField()
form.bind("<Key>", keyPress)
form.mainloop()

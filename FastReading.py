import tkinter as tk
import random as rand
import pprint
import sys, os

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def go():
    global lbl, speed_arr, speed, level
    global easy_phrases, hard_phrases
    global restartB, goB

    #   GETS LEVEL
    if int(level.get())==1:
        index = rand.randint(0,len(easy_phrases))
        tt = easy_phrases[index].split(sep = ' ')
    elif int(level.get())==2:
        index = rand.randint(0,len(hard_phrases))
        tt = hard_phrases[index].split(sep = ' ')

    #   SHOWS 3...2...1...
    delta = 500
    delay = 0
    for i in range(3):
        s = 3-i
        update_text = lambda s=s: lbl.config(text = s)
        lbl.after(delay, update_text)
        delay += delta

    #   SHOWS WORDS
    delta = speed_arr[int(speed.get())-1]
    delay = 1500
    for i in range(len(tt)):
        s = tt[i]
        update_text = lambda s=s: lbl.config(text = s)
        lbl.after(delay, update_text)
        delay += delta
    
    restartB['state'] = 'normal'
    goB['state'] = 'disabled'

def changeLevel(selection):
    global level
    level.set(selection)

def changeSpeed(selection):
    global speed
    speed.set(selection)


#   MAIN

easy_phrases = []
hard_phrases = []

speed_arr = [150, 120, 100, 90, 80, 70, 60, 50]

#   READ PHRASES DATABASE
with open('Db.txt', 'r', encoding='utf-8') as f:
    count = 0
    for line in f:
        if line[:2]!='//':
            if count==0:
                easy_phrases.append(line[:-1])
            elif count==1:
                hard_phrases.append(line[:-1])
        else: count += 1

#   ROOT
root = tk.Tk()
root.geometry('500x300+300+200')
root.wm_attributes("-topmost", 1)
root.columnconfigure((5), weight=1)

#   VARIABLES
level = tk.IntVar()
speed = tk.IntVar()
level.set(1)
speed.set(1)
levelChoices = range(1, 3)
speedChoices = range(1, 9)

#   WIDGETS
lbl = tk.Label(root, text='', font=("Helvetica", 32))
lbl.place(relx=.5, rely=.5, anchor="c")

levelLbl = tk.Label(root, text = 'Level')
levelLbl.grid(row = 0, column = 0)

levelOM = tk.OptionMenu(root, level, *levelChoices, command = changeLevel)
levelOM.grid(row = 0, column = 1)

speedLbl = tk.Label(root, text = 'Speed')
speedLbl.grid(row = 0, column = 2)

speedOM = tk.OptionMenu(root, speed, *speedChoices, command = changeSpeed)
speedOM.grid(row = 0, column = 3)

goB = tk.Button(root, text='Go!', font=("Helvetica", 10), command= lambda: go())
goB.grid(row = 0, column = 4, sticky = 'ne')

restartB = tk.Button(root, text='Restart', font=("Helvetica", 10), command= lambda: restart_program(), state = 'disabled')
restartB.grid(row = 0, column = 5, sticky = 'ne')

#   MAINLOOP
root.mainloop()
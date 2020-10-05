# delay bug, start/stop

from tkinter import *
import time
import pyautogui

# Spam function
def spam(tm, rt):
    time.sleep(tm)
    f = open(rt, 'r')
    for i in f:
        time.sleep(tm)
        pyautogui.typewrite(i)
        pyautogui.press("enter")

# Style variables
bgc = "black"
gfont = ("Helvetica", 12)
fore = "white"

# GUI
main = Tk()
main.config(bg=bgc)
main.title("PythonSpammerTK")
main.resizable(False, False)

app = Frame(main, bg=bgc)
app.grid(padx=30, pady=10)

title = Label(app, text="Select your spam preferences", font=("Helvetica", 20, "bold"), bg=bgc, fg=fore)
title.grid(row=0, column=0, pady=5, padx=5, columnspan=2)

ldelay = Label(app, text="Delay (seconds):", font=gfont, bg=bgc, fg=fore)
ldelay.grid(row=1, column=0, pady=10, padx=5, sticky="w")
cdelay = Entry(app, font=gfont, width=4)
cdelay.grid(row=1, column=1, pady=10, padx=5, sticky="w")

lselect = Label(app, text="File not selected!", font=gfont, bg=bgc, fg="red")
lselect.grid(row=2, column=0, pady=10, padx=5, sticky="w")
bfile = Button(app, text="Select file...", font=gfont) # Add command later
bfile.grid(row=2, column=1, pady=10, padx=5, sticky="w")

lor = Label(app, text="or/and...", font=("Helvetica", 16), bg=bgc, fg=fore)
lor.grid(row=3, column=0, pady=5, padx=5, columnspan=2)

ltext = Label(app, text="Insert spam phrases below...", font=("Helvetica", 10), bg=bgc, fg=fore)
ltext.grid(row=4, column=0, padx=5, sticky="ws")
ttext = Text(app, font=gfont, width=20, height=5)
ttext.grid(row=5, column=0, pady=10, padx=5, columnspan=2, sticky="nsew")
# -----------------------------------------------------------------------------------------------
scrollb = Scrollbar(app, command=ttext.yview)
ttext.config(yscrollcommand=scrollb.set)
scrollb.grid(row=5, column=2, pady=10, sticky="ns")

btrigg = Button(app, text="Let's rock n' roll!", font=("Helvetica", 16, "bold"))
btrigg.grid(row=6, column=0, pady=5, padx=5, columnspan=3, sticky="ew")

main.mainloop()
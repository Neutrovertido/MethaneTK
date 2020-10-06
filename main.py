from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import time
import pyautogui
import threading

# Style variables
bgc = "black"
gfont = ("Helvetica", 12)
fore = "white"

# Spam function
def spam(tm, rt):
    try:
        f = open(rt, 'r', encoding='utf-8')
        time.sleep(tm)
        for i in f:
            if (btrigg['text'] == "Stop the music!"):
                pyautogui.typewrite(i)
                pyautogui.press("enter")
                time.sleep(tm)
    except:
        lselect.config(text="No file was selected", fg="lightgray")
    finally:
        textload = ttext.get("1.0", "end-1c")
        words = textload.split()
        if (len(textload) > 0):
            for i in words:
                if (btrigg['text'] == "Stop the music!"):
                    pyautogui.typewrite(i)
                    pyautogui.press("enter")
                    time.sleep(tm)
        btrigg.config(text="Let's rock n' roll!")

# Start/Stop Button
def goSpam():
    if (btrigg['text'] == "Let's rock n' roll!"):
            try:
                tm = int(cdelay.get())
                rt = lselect["text"]
                btrigg.config(text="Stop the music!")
                spam(tm, rt)
            except:
                messagebox.showerror("Error","Delay must be a number!")
    else:
            btrigg.config(text="Let's rock n' roll!")


# Ask file function
def fileSearch():
    filename = askopenfilename()
    if len(filename) > 0:
        lselect.config(text=filename, fg="green")
    else:
        lselect.config(text="File not selected!", fg="red")

# Clear data function
def clear():
    cdelay.delete(0, "end")
    lselect.config(text="File not selected!", fg="red")
    ttext.delete("1.0", END)

# About function
def about():
    messagebox.showinfo("About","Methane TK - a0.0.1\n⚖GPL-3.0 License\nMade by Neutrovertido!")

# GUI
main = Tk()
main.config(bg=bgc)
main.title("MethaneTK")
main.resizable(False, False)
# main.iconbitmap("./img/forward-32.ico") # Linux doesn't support it
bar = Menu(main)
main.config(menu=bar)

app = Frame(main, bg=bgc)
app.pack(padx=30, pady=15)

title = Label(app, text="Select your spam preferences", font=("Helvetica", 20, "bold"), bg=bgc, fg=fore)
title.grid(row=0, column=0, pady=5, padx=5, columnspan=2)

ldelay = Label(app, text="Delay (seconds):", font=gfont, bg=bgc, fg=fore)
ldelay.grid(row=1, column=0, pady=10, padx=5, sticky="w")
cdelay = Entry(app, font=gfont, width=4)
cdelay.grid(row=1, column=1, pady=10, padx=5, sticky="w")

lselect = Label(app, text="File not selected!", font=gfont, bg=bgc, fg="red")
lselect.grid(row=2, column=0, pady=10, padx=5, sticky="w")
bfile = Button(app, text="Select file...", font=gfont, command=fileSearch)
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

btrigg = Button(app, text="Let's rock n' roll!", font=("Helvetica", 16, "bold"), command=lambda: threading.Thread(target=goSpam).start())
btrigg.grid(row=6, column=0, pady=5, padx=5, columnspan=3, sticky="ew")
# -----------------------------------------------------------------------------------------------
mfile = Menu(bar, tearoff=0)
mfile.add_command(label="New", command=clear)
mfile.add_command(label="Select file...", command=fileSearch)
mfile.add_separator()
mfile.add_command(label="Exit", command=main.quit)

mhelp = Menu(bar, tearoff=0)
mhelp.add_command(label="About", command=about)

bar.add_cascade(label="File", menu=mfile)
bar.add_cascade(label="Help", menu=mhelp)

main.mainloop()

from datetime import datetime
from tkinter import *
from tkinter import ttk


def update_time():
    global currentTime, root
    currentTime.set(datetime.now().strftime("%H:%M:%S"))
    root.after(500, update_time)


root = Tk()
root.title("PyClock")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

currentTime = StringVar()
ttk.Label(mainframe, textvariable=currentTime, font=('Arial', 100)).grid(column=1, row=1, sticky=(W, E))
currentTime.set(datetime.now().strftime("%H:%M:%S"))

root.after(500, update_time)
root.attributes('-topmost', 'true')
root.mainloop();

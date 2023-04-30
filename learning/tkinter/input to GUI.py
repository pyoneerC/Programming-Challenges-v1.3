from tkinter import *

def a(event):
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>", a)

label = Label(window, font=("Helvetica", 100)) # label is a widget of the Tkinter library that is used to display text in a GUI window
label.pack()

window.mainloop()

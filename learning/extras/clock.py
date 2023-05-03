from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p") # clock (hours, minutes, seconds, PM/AM)
    time_label.config(text=time_string)  # assigning value o time_string

    day_string = strftime("%A") # day
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y") # format (month day year)
    date_label.config(text=date_string)

    window.after(1000,update) # updates per second


window = Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black") # timer
time_label.pack() # we pack all elements for they to display correctly 

day_label = Label(window,font=("Ink Free",25,"bold")) # day
day_label.pack()

date_label = Label(window,font=("Ink Free",30)) # date
date_label.pack()

update()

# The update() function is defined which gets the current time, day, and date using the strftime() function from the time module. The strftime() function formats the date and time according to the specified format string.

window.mainloop()
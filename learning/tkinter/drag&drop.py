# import the tkinter module for GUI creation
from tkinter import *

# define a function to handle the starting of a drag event
def drag_start(event):
    widget = event.widget  # get the widget that was clicked
    widget.startX = event.x  # save the x coordinate of the click event in the widget's attributes
    widget.startY = event.y  # save the y coordinate of the click event in the widget's attributes

# define a function to handle the motion of a drag event
def drag_motion(event):
    widget = event.widget  # get the widget that is being dragged
    # calculate the new position of the widget based on the difference between the current position and the starting position of the drag event
    x = widget.winfo_x() - widget.startX + event.x #  winfo_x() returns the x-coordinate. formula calculates the new x-coordinate of the widget by subtracting the starting x-coordinate from the current x-coordinate of the mouse pointer within the widget, and adding the result to the current x-coordinate of the widget relative to its parent window.
    y = widget.winfo_y() - widget.startY + event.y #  same formula as above but with 'y'
    widget.place(x=x,y=y)  # move the widget to the new position

# Formula: current x-coordinate position of a widget relative to its parent widget - starting position + current
# The parent widget is the main window created with window = Tk() (almost every time,  it's also possible to create other containers (such as Frame or Toplevel widgets) that can act as parent widgets for other widgets), which holds the two labels created with label = Label(window,...) and label2 = Label(window,...). The window is created using the Tk() function and all the widgets are added to it using the place() method.

# create a new Tkinter window, obligatory
window = Tk()

# Label with L(abel)

# create a red label widget (with certain specifications, such a width an height) and place it in the window
label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0) # starting position red square

# create a blue label widget and place it in the window
label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100) # starting position blue square

# bind the drag_start and drag_motion functions to the left mouse button events of the labels
label.bind("<Button-1>",drag_start) # Click trigger function (left mouse)
label.bind("<B1-Motion>",drag_motion) # Each pixel moves triggers the function

label2.bind("<Button-1>",drag_start) # Click trigger function (left mouse)
label2.bind("<B1-Motion>",drag_motion) # Each pixel moves triggers the function

# start the main event loop for the window
window.mainloop() # ---> Tk.mainloop()

# window.mainloop() is necessary in most cases when using Tkinter, as it starts the main event loop for the application. This loop listens for and handles events such as mouse clicks and key presses, and updates the GUI accordingly. Without this loop, the window would be displayed but would not respond to any user input.

# The mainloop() method blocks the program until the user closes the window or calls window.quit(), which terminates the event loop and ends the program.

# Since label2 is placed after label, it is stacked on top of label. This means that any part of label2 that overlaps with label will be displayed on top of label, which gives the impression that label2 is "going through" label.

# When the labels are dragged using the drag_motion function, their positions are updated using the place() method with the new coordinates, but their stacking order remains the same. This means that if label2 is dragged over label, it will still be displayed on top of label.
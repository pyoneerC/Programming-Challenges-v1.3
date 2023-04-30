from tkinter import *

window = Tk() #  The Tk() function initializes the Tkinter interpreter and creates an instance of a Tkinter application window. This function returns the instance of the main window, which is then used to add widgets and components to the GUI.

canvas = Canvas(window,height=500,width=500)
canvas.create_arc(0,0,450,450,style=PIESLICE,start=180,width=5)
canvas.create_arc(0,0,450,450,fill="yellow",extent=270,start=180,width=10) # Extent change how much range it cover, while start means where the shape starts
canvas.create_oval(40,40,150,150,fill="red",outline="black",width=5)
canvas.create_oval(300, 40, 375, 150, fill="white", outline="black", width=5)

# Commented examples:

#canvas.create_line(0,0,500,500,fill="blue",width=5) # 0,0 is where the line starts (x,y) and the 500,500 is where it ends.
#canvas.create_line(0,500,500,0,fill="red",width=5)
#canvas.create_rectangle(50,50,250,250,fill="purple")
#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill="yellow",outline="black",width=5)
# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)

# Other tip is that latest (newest) code has priority and will go above ('overwrite') the shapes of the previous lines, just like CSS.

# It's all a grid that goes from 0-500 in both axis, from top left corner to low right corner. Take that in mind for placing and drawing in a canvas.

canvas.pack()

window.mainloop()


# The window.mainloop() method is a blocking method that starts the event loop of the tkinter application. It listens to user events such as mouse clicks, keyboard inputs, etc. and updates the GUI accordingly.

# This method should be called only once at the end of the script after all the widgets and components have been added to the GUI. It keeps the window o}pen and active until the user closes the window or the program is terminated.
from tkinter import *

def doSomething(event):
    print(f'x:{str(event.x)}, y: {str(event.y)}') # Shows x and y coords

window = Tk() # Default is 200x200px, like in this case

#               button:     func
# window.bind("<Button-1>",doSomething) #left mouse click
window.bind("<Button-2>",doSomething) #scroll wheel
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething)# mouse button release, we call doSomething func
#window.bind("<Enter>",doSomething) #enter the window
#window.bind("<Leave>",doSomething) #leave the window
#window.bind("<Motion>",doSomething) #Where the mouse moved (every position)
window.mainloop()
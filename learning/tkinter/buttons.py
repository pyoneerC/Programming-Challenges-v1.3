from tkinter import *

from tkinter import *

root = Tk()

label1 = Label(root, text='abc') # Details, colors, text, action, etc. (see below examples)
label1.pack(side=TOP, expand=True) # In the packing we specify side and if expands or not, all else in the Label()

label2 = Label(root, text="you sure?", fg="blue")
label2.pack(side=TOP, expand=True)

button1 = Button(root, text='Accept', fg="green", command=root.destroy)
button1.pack(side=LEFT, expand=True)

button2 = Button(root, text='Close', fg='red', command=root.destroy)
button2.pack(side=RIGHT, expand=True)

root.mainloop()

# fg ---> foreground
from tkinter import *

##In tkinter everything is widget and first we need to create root widget

'''
    1.Define/Create the thing
    2.Add it to screen
'''
root=Tk()
myLabel=Label(root,text='Banoth Srikanth')

'''
    couple of ways to add widgets to tkinter 1.pack (unsophisticated)
    be like what it is
'''

myLabel.pack()

##Create an Event loop always loop constant loop


root.mainloop()



'''
Grid System Python
'''

from tkinter import *

root=Tk()

firstname=Label(root,text='Banoth')
lastname=Label(root,text='Srikanth')

'''
Pack using grid system
'''

firstname.grid(row=0,column=0)
lastname.grid(row=1,column=1);


root.mainloop()

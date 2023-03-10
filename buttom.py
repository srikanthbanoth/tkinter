import tkinter

root=tkinter.Tk()
'''
fg=foregroundcolor
bg=backgroundcolor
'''
def myClick():
    label=tkinter.Label(root,text='You clicked me')
    label.pack()

button=tkinter.Button(root,text='click',padx=10,command=myClick)
button.pack()


root.mainloop()

import tkinter

def show_entry_fields():
    print("First Name: {}\nLast Name: {}".format(e1.get(), e2.get()))

master = tkinter.Tk()
##tkinter.Label(master, text="First Name").grid(row=0)
##tkinter.Label(master, text="Last Name").grid(row=1)
##
##e1 = tkinter.Entry(master)
##e2 = tkinter.Entry(master)
##
##e1.grid(row=0, column = 1)
##e2.grid(row=1, column=1)
##
##tkinter.Button(master, text='Quit', command=master.quit).grid(row=3, column = 0, sticky = tkinter.W, pady = 4)
##tkinter.Button(master, text = 'Show', command=show_entry_fields).grid(row=3, column = 1, sticky=tkinter.W, pady=4)

def printSomething():
    for x in range(9):
        label = tkinter.Label(master, text=str(x))
        label.pack()

tkinter.Button(master, text="Print Me", command=printSomething).grid(row=4, column=0, sticky=tkinter.W)

master.mainloop()

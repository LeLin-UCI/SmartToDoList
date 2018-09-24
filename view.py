from tkinter import Tk,Entry, Label, mainloop, Button, N, S, W, E
import model

root = Tk()

#make_task = tkinter.Button(root, text="Enter", command=model.

enter_name          = Entry(root)
enter_duedate       = Entry(root)
enter_difficulty    = Entry(root)
enter_description   = Entry(root)

name_label          = Label(root, text="Name").grid(        row=5, column=0, sticky=W)
duedate_label       = Label(root, text="Due Date").grid(    row=5, column=1, sticky=W)
difficulty_label    = Label(root, text="Difficulty").grid(  row=5, column=2, sticky=W)
description_label   = Label(root, text="Description").grid( row=7, column=0, sticky=W)

enter_name.grid(        row=6, column=0)
enter_duedate.grid(     row=6, column=1)
enter_difficulty.grid(  row=6, column=2)
enter_description.grid( row=8, column=0)

maker = Button(root,
               text="Add Task",
               command=model.make_task(enter_name,
                                       enter_duedate,
                                       enter_difficulty,
                                       enter_description)).grid(row=9, sticky=W)
def print_print():
    print("Yeah")

test = Button(root, text="Test", command = print_print).grid(row=9, column=10, sticky=W)

if __name__ == '__main__':
    mainloop()

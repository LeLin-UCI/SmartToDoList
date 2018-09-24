"""
TO DO: 
add task to the text widget, maybe switch to canvas widget?
make the sorting algorithm based on the priority of tasks
fully implement the datetime objects
when you press add task, clear the entry widgets
make the window resizable
"""
## Last updated 8/1/2018

import tkinter
import model


class ToDoListApp:
    def __init__(self):
        """Creating a root window and initializing the ToDoList model.
        """
        self.tdl = model.ToDoList()

        self.root = tkinter.Tk()
        self.setup()

    def run(self):
        """Setting up then running.
        """
##        self.setup()
        tkinter.mainloop()

    def setup(self):
        """Setting up all of the entry widgets and the labels. Then setting up
        the main display.
        """
        ## Entry widgets and corresponding labels
        name = tkinter.Label(self.root, text="Name").grid(row=5, column=0, sticky=tkinter.W)
        self.enter_name = tkinter.Entry(self.root)
        self.enter_name.grid(row=6, column=0)
        
        duedate = tkinter.Label(self.root, text="Due Date").grid(row=5, column=1, sticky=tkinter.W)
        self.enter_duedate = tkinter.Entry(self.root)
        self.enter_duedate.grid(row=6, column=1)
        
        difficulty = tkinter.Label(self.root, text="Difficulty").grid(row=5, column=2, sticky=tkinter.W)
        self.enter_difficulty = tkinter.Entry(self.root)
        self.enter_difficulty.grid(row=6, column=2)
        
        description = tkinter.Label(self.root, text="Description").grid(row=7, column=0, sticky=tkinter.W)
        self.enter_description = tkinter.Entry(self.root)
        self.enter_description.grid(row=8, column=0)

        self.fields = [self.enter_name, self.enter_duedate, self.enter_difficulty, self.enter_description]

        ## Main Display window
        self.display = tkinter.Text(self.root, height=len(self.tdl)*2, width = 50)
        self.display.grid(row=0, column=0, columnspan=3)
        
        ## Add Task button
        maker = tkinter.Button(self.root, text="Add Task", command=self.add_task).grid(row=9, sticky=tkinter.W)

    def add_task(self):
##        print(type(self.enter_name))
        for field in self.fields:
            if field.get() == '':
                empty_message = tkinter.Label(self.root, text="One of the fields is empty!").grid(row=9, columnspan=3)
            else:
                empty_message.grid_forget()  ## Doesn't work
                self.tdl.add(model.Task(self.enter_name.get(), self.enter_duedate.get(), self.enter_difficulty.get(), self.enter_description.get()))
        

if __name__ == '__main__':
    T = ToDoListApp()
    T.run()


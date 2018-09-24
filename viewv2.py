"""
TO DO: 
add task to the text widget, maybe switch to canvas widget?
make the sorting algorithm based on the priority of tasks
fully implement the datetime objects
when you press add task, clear the entry widgets
make the window resizable

9/16/2018 CHANGELOG:
    added way to check if the fields were empty or not by using custom exception
    cleared the empty field message
    added method to display tasks from todolist but its not working
    
"""
## Last updated 8/1/2018
## Last updated 9/16/2018

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
        #self.display = tkinter.Text(self.root, height=len(self.tdl)*2, width = 50)
        #self.display.grid(row=0, column=0, columnspan=3)
        
        ## Add Task button
        maker = tkinter.Button(self.root, text="Add Task", command=self.add_task).grid(row=9, sticky=tkinter.W)


    def add_taska(self):
##        print(type(self.enter_name))
        for field in self.fields[:-1]:
            if field.get() == '':
                empty_message = tkinter.Label(self.root, text="One of the fields is empty!").grid(row=9, columnspan=3)
                #empty_message.grid_forget()  ## Doesn't work
        self.tdl.add(model.Task(self.enter_name.get(), self.enter_duedate.get(), self.enter_difficulty.get(), self.enter_description.get()))
        print(self.tdl.lot)

    def add_task(self):
        for label in self.root.grid_slaves():  # This method of clearing the empty field message might break later once we add label widgets to the top.
            # print(label.grid_info())
            if label.grid_info()["row"] == 9 and label.grid_info()["columnspan"] == 3:
                label.grid_forget()
        try:
            self.tdl.add(model.Task(self.enter_name.get(), self.enter_duedate.get(), self.enter_difficulty.get(), self.enter_description.get()))
           #print(self.tdl.lot)
        except model.EmptyFieldError:
            empty_message = tkinter.Label(self.root, text="One of the fields is empty!").grid(row=9, columnspan=3)

    def display_tasks(self):
        print("here")
        print(len(self.tdl.lot))
        for x in range(len(self.tdl.lot)):
            tkinter.Label(self.root, text=str(self.tdl.lot[x])).grid(row=x)
            
        

if __name__ == '__main__':
    T = ToDoListApp()
    T.run()


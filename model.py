import datetime
import re

class Task:

    def __init__(self, name: str, duedate: (int), difficulty: int, description = ' '):
        self.name = name
        #self.duedate = datetime.date(*duedate)
##        print(type(duedate))
        self.duedate = duedate
        self.difficulty = difficulty
        self.check_fields() # checks all the fields before checks decsription, probably a better way to do this
                            # bandaid solution to make it work with how i decided to check if all info was put in  
        self.description = description
##        self.check_fields()

    def get_name(self):
        return self.name

    def get_duedate(self):
        return self.duedate

    def get_difficulty(self):
        return self.difficulty

    def get_description(self):
        return self.description

    def check_fields(self):
        print(self.__dict__.items())
        for item in self.__dict__:
            if self.__dict__[item] == '':
                raise EmptyFieldError

    def __str__(self):
        return '{} {} {} \n{}'.format(self.name, self.duedate, self.difficulty, self.description)

    @staticmethod
    def _check_format():
        pass

class EmptyFieldError(Exception):
    pass     

class ToDoList:

    def __init__(self, lot: [Task] = []):
        self.lot = lot # List of Task
    
    def add(self, arg: Task):
        if type(arg) != Task:
            return NotImplemented
        self.lot.append(arg)

    def __len__(self):
        return len(self.lot)
##    @staticmethod
##    def init():
##        return ToDoList()


if __name__ == '__main__':
##    wow = ToDoList.init()
##    print(type(wow))
##    pass
    wow = ToDoList()
    print(type(wow))

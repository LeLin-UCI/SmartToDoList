import tkinter as tk

class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self).pack()
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
##        self.entry.pack()

    def on_button(self):
        print(type(self.entry))
        print(self.entry.get())

w = SampleApp()
w.mainloop()

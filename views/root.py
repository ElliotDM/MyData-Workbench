from tkinter import Tk


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("MyWorkbench")
        self.geometry('400x200')
        self.resizable(False,False)
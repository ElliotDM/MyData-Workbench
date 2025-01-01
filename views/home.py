from tkinter.ttk import (
    Frame,
    Style,
    Notebook,
    Label,
    Combobox,
    Button,
    Panedwindow)
from tkinter import HORIZONTAL


class Home(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.style = Style(master)
        self.style.theme_use('forest-light')

        self.notebook = Notebook(self, width=790, height=590)

        ### tab_1
        self.tab_1 = Frame(self.notebook)
        self.tab_1.columnconfigure(index=0, weight=0)
        self.tab_1.columnconfigure(index=1, weight=0)
        self.tab_1.rowconfigure(index=0, weight=0)
        self.tab_1.rowconfigure(index=1, weight=0)
        self.notebook.add(self.tab_1, text="View")

        self.combobox = Combobox(self.tab_1)
        self.combobox.grid(row=0, column=0, padx=(0, 10), sticky="w")

        self.button = Button(self.tab_1, text="Hi")
        self.button.grid(row=0, column=1, padx=(0, 10), sticky="w")

        self.label = Label(self.tab_1, text="Hi", justify="center")
        self.label.grid(row=1, column=0, pady=10, columnspan=2)

        # Tab_2
        self.tab_2 = Frame(self.notebook)

        self.notebook.add(self.tab_2, text="Statistics")

        #Tab_3
        self.tab_3 = Frame(self.notebook)

        self.notebook.add(self.tab_3, text="Analysis")

        self.notebook.grid(row=0, column=0, sticky='e')

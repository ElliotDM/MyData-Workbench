from tkinter.ttk import Style, Label, Combobox, Entry, Button, Frame


class Home(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.style = Style(master)
        self.style.theme_use('forest-light')

        self.table_label = Label(self, text="Select table")
        self.table_combobox = Combobox(self, state="readonly")
        
        self.table_label.grid(row=0, column=0, padx=10, sticky="w")
        self.table_combobox.grid(row=0, column=1, padx=(0, 20), sticky="ew")

        self.search_label = Label(self, text="Search by")
        self.search_combobox = Combobox(self, state="readonly")
        
        self.search_label.grid(row=1, column=0, padx=10, sticky="w")
        self.search_combobox.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        self.field_entry = Entry(self)
        self.search_btn = Button(self, text="Search")

        self.field_entry.grid(row=2, column=0, padx=(0, 20), sticky="ew")
        self.search_btn.grid(row=2, column=1, padx=0, pady=10, sticky="w")

        self.frame = Frame(self)
        self.frame.grid(row=3, column=0)
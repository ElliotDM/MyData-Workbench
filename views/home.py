from tkinter.ttk import (
    Frame,
    Style,
    Notebook,
    Label,
    Combobox,
    Button,
    Panedwindow,
    Treeview)
from tkinter import PhotoImage

class Home(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.style = Style(master)
        self.style.theme_use('forest-light')

        self.notebook = Notebook(self, width=790, height=590)

        ### tab_1
        self.tab_1 = Frame(self.notebook)

        self.tab_1.columnconfigure(index=0, weight=1)
        self.tab_1.columnconfigure(index=1, weight=0)
        self.tab_1.columnconfigure(index=2, weight=0)
        self.tab_1.columnconfigure(index=3, weight=0)
        self.tab_1.columnconfigure(index=4, weight=0)
        self.tab_1.columnconfigure(index=5, weight=0)
        self.tab_1.columnconfigure(index=6, weight=0)
        self.tab_1.columnconfigure(index=7, weight=0)
        self.tab_1.columnconfigure(index=8, weight=0)
        self.tab_1.columnconfigure(index=9, weight=0)

        self.tab_1.rowconfigure(index=0, weight=0)
        self.tab_1.rowconfigure(index=1, weight=7)
        self.tab_1.rowconfigure(index=2, weight=1)

        self.notebook.add(self.tab_1, text="View")

        self.database_combobox = Combobox(self.tab_1)
        self.database_combobox.grid(row=0, column=0,
                                    padx=(0, 10), sticky="ew")

        self.folder_photo = PhotoImage(file='icons/folder.png')
        self.folder_icon = self.folder_photo.subsample(12, 12)

        self.open_btn = Button(self.tab_1,
                               image=self.folder_icon)
        self.open_btn.grid(row=0, column=1, padx=(0, 10), sticky="ew")

        self.new_query_photo = PhotoImage(file='icons/new_query.png')
        self.new_query_icon = self.new_query_photo.subsample(12, 12)

        self.new_query_btn = Button(self.tab_1,
                                    image=self.new_query_icon)
        self.new_query_btn.grid(row=0, column=2, padx=(0, 10), sticky="ew")

        self.save_photo = PhotoImage(file='icons/save.png')
        self.save_icon = self.save_photo.subsample(12, 12)

        self.save_btn = Button(self.tab_1,
                               image=self.save_icon)
        self.save_btn.grid(row=0, column=3, padx=(0, 10), sticky="ew")

        self.exec_photo = PhotoImage(file='icons/exec.png')
        self.exec_icon = self.exec_photo.subsample(12, 12)

        self.exec_btn = Button(self.tab_1,
                               text='Execute',
                               image=self.exec_icon,
                               compound="left")
        self.exec_btn.grid(row=0, column=4, padx=(0, 10), sticky="ew")

        self.stop_photo = PhotoImage(file='icons/stop.png')
        self.stop_icon = self.stop_photo.subsample(12, 12)

        self.stop_btn = Button(self.tab_1,
                               image=self.stop_icon)
        self.stop_btn.grid(row=0, column=5, padx=(0, 10), sticky="ew")

        self.undo_photo = PhotoImage(file='icons/undo.png')
        self.undo_icon = self.undo_photo.subsample(12,12)

        self.undo_btn = Button(self.tab_1,
                               image=self.undo_icon)
        self.undo_btn.grid(row=0, column=6, padx=(0, 10), sticky="ew")

        self.redo_photo = PhotoImage(file='icons/redo.png')
        self.redo_icon = self.redo_photo.subsample(12,12)

        self.redo_btn = Button(self.tab_1,
                               image=self.redo_icon)
        self.redo_btn.grid(row=0, column=7, padx=(0, 10), sticky="ew")

        self.find_photo = PhotoImage(file='icons/find.png')
        self.find_icon = self.find_photo.subsample(12,12)

        self.find_btn = Button(self.tab_1,
                               image=self.find_icon)
        self.find_btn.grid(row=0, column=8, padx=(0, 10), sticky="ew")

        self.replace_photo = PhotoImage(file='icons/replace.png')
        self.replace_icon = self.replace_photo.subsample(12,12)

        self.replace_btn = Button(self.tab_1,
                                  image=self.replace_icon)
        self.replace_btn.grid(row=0, column=9, padx=(0, 10), sticky="ew")

        self.paned_win1 = Panedwindow(self.tab_1, orient="horizontal")
        self.paned_win1.grid(row=1, column=0, columnspan=10,
                             padx=(0, 10), pady=(0,10), sticky="nsew")

        self.tree = Treeview(self.paned_win1)
        self.tree.heading('#0', text='Schemas', anchor='w')
        self.tree.grid(columnspan=2, sticky="ns")

        self.pane2 = Label(self.paned_win1,
                           text="Pane 2",
                           justify="center")

        self.paned_win1.add(self.tree)
        self.paned_win1.add(self.pane2)

        self.label = Button(self.tab_1,
                           text="Status bar")

        self.label.grid(row=2, column=0,
                        columnspan=10, padx=(0, 10), sticky='nsew')

        # Tab_2
        self.tab_2 = Frame(self.notebook)

        self.notebook.add(self.tab_2, text="Statistics")

        #Tab_3
        self.tab_3 = Frame(self.notebook)

        self.notebook.add(self.tab_3, text="Analysis")

        self.notebook.grid(row=0, column=0, sticky='nsew')

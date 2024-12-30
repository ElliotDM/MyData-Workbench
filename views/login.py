from tkinter.ttk import Style, Entry, Label, Button, Frame


class LogIn(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.style = Style(master)
        self.style.theme_use('forest-light')

        self.header = Label(self, text="Sign In with existing account")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.user_label = Label(self, text="User: ")
        self.user_entry = Entry(self)

        self.user_label.grid(row=1, column=0, padx=10, sticky="e")
        self.user_entry.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        self.host_label = Label(self, text="Host: ")
        self.host_entry = Entry(self)

        self.host_label.grid(row=2, column=0, padx=10, sticky="e")
        self.host_entry.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password: ")
        self.password_entry = Entry(self, show='*')

        self.password_label.grid(row=3, column=0, padx=10, sticky="e")
        self.password_entry.grid(row=3, column=1, padx=(0, 20), sticky="ew")

        self.login_btn = Button(self, text="Sign In",
                                style="ToggleButton")
        self.login_btn.grid(row=4, column=1, padx=0, pady=10, sticky="w")
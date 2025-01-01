from views.root import Root
from views.login import LogIn
from views.home import Home


class View:
    def __init__(self):
        self.root = Root()
        self.root.option_add("*tearOff", False)
        self.root.call('source', 'forest-light.tcl')

        self.frames = {}

        self._add_frame(LogIn, "login")
        self._add_frame(Home, "home")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def resize(self, width, height):
        self.root.geometry(f'{width}x{height}')
        self.root.update()

    def star_mainloop(self):
        self.root.mainloop()
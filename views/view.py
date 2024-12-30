from .root import Root
from .login import LogIn
from .home import Home


class View:
    def __init__(self):
        self.root = Root()
        self.root.option_add("*tearOff", False)
        self.root.call('source', 'forest-light.tcl')

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.frames = {}

        self._add_frame(LogIn, "login")
        self._add_frame(Home, "home")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def swicth(self, name):
        frame = self.frames[name]
        frame.tkraise()
        self.root.update()

    def resize(self, width, hegiht):
        self.root.geometry(f'{width}x{hegiht}')

    def star_mainloop(self):
        self.root.mainloop()
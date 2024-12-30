from .home import HomeController
from .login import LogInController


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.login_controller = LogInController(model, view)
        self.home_controller = HomeController(model, view)
        self.model.auth.add_event_listener(
            "auth_changed", self.auth_state_listener
        )

    def auth_state_listener(self, data):
        if data:
            self.view.swicth("home")
            self.view.resize(self.view.width, self.view.height)
        else:
            self.view.swicth("login")
            self.view.resize(400, 200)

    def start(self):
        if self.model.auth.is_logged_in:
            self.view.swicth("home")
        else:
            self.view.swicth("login")

        self.view.star_mainloop()


class LogInController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["login"]
        self._bind()

    def _bind(self):
        self.frame.login_btn.config(command=self.login)

    def login(self):
        user = self.frame.user_entry.get()
        host = self.frame.host_entry.get()
        password = self.frame.password_entry.get()
        self.frame.password_entry.delete(0, last=len(password))

        if error := self.model.auth.login(host, user, password):
            self.frame.error_message(error)
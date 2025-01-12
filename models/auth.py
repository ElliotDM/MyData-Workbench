from mysql.connector.errors import get_mysql_exception
from models.observer import Observer
import mysql.connector


class Auth(Observer):
    def __init__(self):
        super().__init__()
        self.is_logged_in = False
        self.connection = None

    def login(self, host, user, password):
        self.is_logged_in = True

        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
            )

            self.trigger_event("auth_changed")
        except mysql.connector.Error as error:
            return error

    def logout(self):
        self.is_logged_in = False
       
        if self.connection is not None:
            self.connection.close()
            self.connection = None

        self.trigger_event("auth_changed")
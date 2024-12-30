from models.model import Model
from views.view import View
from controllers.controller import Controller


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start()


if __name__ == '__main__':
    main()
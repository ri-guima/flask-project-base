from flask import Flask

from .app import create_app


class Extension:

    def __init__(self, app: Flask) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        pass

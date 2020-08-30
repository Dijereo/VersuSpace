from screen import *
from rocket import *


class GameScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.rocket = Rocket((app.width // 2, app.height // 2), 0, Colors.RED)

    def draw(self, window):
        window.fill(Colors.BLACK)
        self.rocket.draw(window)

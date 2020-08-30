from screen import *
from rocket import *


class GameScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.rocket = Rocket((app.width // 2, app.height // 2), 0, Colors.RED)
        self.handler.add_state_listeners([ThrustListener(self.rocket)])

    def draw(self, window):
        window.fill(Colors.BLACK)
        self.rocket.move(0.03, (self.width, self.height))
        self.rocket.draw(window)

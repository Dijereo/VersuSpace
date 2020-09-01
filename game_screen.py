from screen import *
from rocket import *


class GameScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.rocket = Rocket((app.width // 4, app.height // 4), 270, Colors.RED)
        self.rocket2 = Rocket((3 * app.width // 4, 3 * app.height // 4), 90, Colors.BLUE)
        self.handler.add_state_listeners([
            ThrustListener(self.rocket, pygame.K_UP),
            RotationListener(self.rocket, pygame.K_RIGHT, pygame.K_LEFT),
            ThrustListener(self.rocket2, pygame.K_w),
            RotationListener(self.rocket2, pygame.K_a, pygame.K_d)
        ])

    def step(self, time):
        self.rocket.move(time, (self.width, self.height))
        self.rocket2.move(time, (self.width, self.height))

    def draw(self, window):
        window.fill(Colors.BLACK)
        self.rocket.draw(window)
        self.rocket2.draw(window)

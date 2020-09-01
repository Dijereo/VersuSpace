from screen import *
from rocket import *


class GameScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        rocket_data = [
            (app.width // 4, app.height // 4, 270, Colors.RED, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_SLASH),
            (3 * app.width // 4, 3 * app.height // 4, 90, Colors.BLUE, pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_e)]
        self.rockets = []
        for posx, posy, angle, color, thrust_key, cw_key, ccw_key, shoot_key in rocket_data:
            self.rockets.append(Rocket((posx, posx), angle, color))
            self.handler.add_state_listeners([
                ThrustListener(self.rockets[-1], thrust_key),
                RotationListener(self.rockets[-1], cw_key, ccw_key)])
            self.handler.add_event_listeners([
                ShootListener(self.rockets[-1], shoot_key)])

    def step(self, time):
        for rocket in self.rockets:
            rocket.move(time, (self.width, self.height))

    def draw(self, window):
        window.fill(Colors.BLACK)
        for rocket in self.rockets:
            rocket.draw(window)

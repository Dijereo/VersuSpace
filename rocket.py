from event import *


class Rocket:
    def __init__(self, pos, angle, color):
        self.pos = pos
        self.angle = angle
        self.color = color

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.get_polygon())

    def get_polygon(self):
        return [(50, 50), (50, 100), (100, 50)]

    def set_thrust(self, on):
        self.color = (255, 0, 0) if on else (0, 0, 255)


class ThrustListener(KeyPressedListener):
    def __init__(self, rocket):
        self.rocket = rocket
        super(ThrustListener, self).__init__(pygame.K_UP)

    def perform_action(self):
        self.rocket.set_thrust(True)

    def perform_alternative(self):
        self.rocket.set_thrust(False)

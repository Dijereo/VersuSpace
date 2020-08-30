from pygame.math import Vector2

from event import *


class Rocket:
    def __init__(self, pos, angle, color):
        self.pos = pos
        self.angle = angle
        self.color = color
        self.thrust = False

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.get_polygon())

    def get_polygon(self):
        vertex1 = Vector2()
        vertex1.from_polar((25, self.angle - 15))
        vertex1 = self.pos - vertex1
        vertex2 = Vector2()
        vertex2.from_polar((25, self.angle + 15))
        vertex2 = self.pos - vertex2
        return [self.pos, vertex1, vertex2]

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

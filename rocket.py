from pygame.math import Vector2

from event import *


class Rocket:
    def __init__(self, pos, angle, color):
        self.pos = Vector2(pos)
        self.velocity = Vector2(1, 1)
        self.acceleration = Vector2(-0.001, -0.002)
        self.angle = angle
        self.color = color
        self.thrust = False

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.get_polygon())

    def move(self, dt, screen_size):
        self.pos += dt * self.velocity
        self.velocity += dt * self.acceleration
        self.try_wrap(screen_size[0], screen_size[1])

    def get_polygon(self):
        vertex1 = Vector2()
        vertex1.from_polar((25, self.angle - 15))
        vertex1 = self.pos - vertex1
        vertex2 = Vector2()
        vertex2.from_polar((25, self.angle + 15))
        vertex2 = self.pos - vertex2
        return [self.pos, vertex1, vertex2]

    def set_thrust(self, on):
        self.thrust = on

    def try_wrap(self, width, height):
        if self.pos.x < 0:
            self.pos.x = width
        elif self.pos.x > width:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = height
        elif self.pos.y > height:
            self.pos.y = 0


class ThrustListener(KeyPressedListener):
    def __init__(self, rocket):
        self.rocket = rocket
        super(ThrustListener, self).__init__(pygame.K_UP)

    def perform_action(self):
        self.rocket.set_thrust(True)

    def perform_alternative(self):
        self.rocket.set_thrust(False)

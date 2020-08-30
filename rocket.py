from pygame.math import Vector2

from event import *


class Rocket:
    def __init__(self, pos, angle, color):
        self.position = Vector2(pos)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(-0.005, -0.004)
        self.angular = 0
        self.angle = angle
        self.color = color
        self.thrust = False

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.get_polygon())

    def move(self, dt, screen_size):
        self.position += dt * self.velocity
        self.velocity += dt * self.acceleration
        self.try_wrap(screen_size[0], screen_size[1])

    def get_polygon(self):
        vertex1 = Vector2()
        vertex1.from_polar((16, self.angle))
        vertex1 = vertex1 + self.position
        vertex2 = Vector2()
        vertex2.from_polar((12, self.angle + 225))
        vertex2 = self.position + vertex2
        vertex3 = Vector2()
        vertex3.from_polar((12, self.angle - 225))
        vertex3 = self.position + vertex3
        return [vertex1, vertex2, vertex3]

    def set_thrust(self, on):
        self.thrust = on

    def try_wrap(self, width, height):
        if self.position.x < 0:
            self.position.x = width
        elif self.position.x > width:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = height
        elif self.position.y > height:
            self.position.y = 0


class ThrustListener(KeyPressedListener):
    def __init__(self, rocket):
        self.rocket = rocket
        super(ThrustListener, self).__init__(pygame.K_UP)

    def perform_action(self):
        self.rocket.set_thrust(True)

    def perform_alternative(self):
        self.rocket.set_thrust(False)

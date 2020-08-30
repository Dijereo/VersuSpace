from pygame.math import Vector2

from event import *


class Rocket:
    def __init__(self, pos, angle, color):
        self.position = Vector2(pos)
        self.velocity = Vector2(0, 0)
        self.angular = 0
        self.angle = angle
        self.color = color
        self.engine_on = False

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.get_polygon())

    def move(self, dt, screen_size):
        self.position += dt * self.velocity
        self.velocity += dt * self.get_acceleration()
        self.try_wrap(screen_size[0], screen_size[1])
        self.angle += self.angular

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

    def get_acceleration(self):
        thrust = Vector2()
        if self.engine_on:
            thrust.from_polar((200, self.angle))
        drag = -0.2 * self.velocity
        return thrust + drag

    def set_engine_state(self, on):
        self.engine_on = on

    def set_rotation(self, direction):
        self.angular = 5 * direction

    def try_wrap(self, width, height):
        if self.position.x < 0:
            self.position.x += width
        elif self.position.x > width:
            self.position.x -= width
        if self.position.y < 0:
            self.position.y += height
        elif self.position.y > height:
            self.position.y -= height


class ThrustListener(KeyPressedListener):
    def __init__(self, rocket):
        super().__init__(pygame.K_UP)
        self.rocket = rocket

    def perform_action(self):
        self.rocket.set_engine_state(True)

    def perform_alternative(self):
        self.rocket.set_engine_state(False)


class RotationListener(StateListener):
    def __init__(self, rocket):
        super().__init__()
        self.rocket = rocket
        self.direction = 0

    def state_occurred(self):
        self.direction = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.direction += 1
        elif pressed[pygame.K_LEFT]:
            self.direction -= 1
        return self.direction != 0

    def perform_action(self):
        self.rocket.set_rotation(self.direction)

    def perform_alternative(self):
        self.rocket.set_rotation(0)

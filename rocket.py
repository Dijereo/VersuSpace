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
        self.bullets = []

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.get_vertices())
        for bullet in self.bullets:
            bullet.draw(window)

    def move(self, dt, screen_size):
        self.position += dt * self.velocity
        self.velocity += dt * self.get_acceleration()
        self.wrap_position(screen_size[0], screen_size[1])
        self.angle += self.angular
        for bullet in self.bullets:
            bullet.move(dt)

    def shoot(self):
        self.bullets.append(Bullet(self.color, self.get_vertices()[1], self.angle, 500))

    def get_vertices(self):
        vertices = [Vector2() for _ in range(3)]
        pos_offsets = [12, 16, 12]
        angle_offsets = [-225, 0, 225]
        for i in range(len(vertices)):
            vertices[i].from_polar((pos_offsets[i], self.angle + angle_offsets[i]))
            vertices[i] += self.position
        return vertices

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

    def wrap_position(self, width, height):
        self.position.x %= width
        self.position.y %= height


class Bullet:
    def __init__(self, color, position, direction, speed):
        self.color = color
        self.position = position
        self.velocity = Vector2()
        self.velocity.from_polar((speed, direction))
        self.radius = 3

    def draw(self, window):
        pygame.draw.circle(window, self.color, tuple(map(round, self.position)), self.radius)

    def move(self, dt):
        self.position += dt * self.velocity


class ThrustListener(KeyPressedListener):
    def __init__(self, rocket, key):
        super().__init__(key)
        self.rocket = rocket

    def perform_action(self):
        self.rocket.set_engine_state(True)

    def perform_alternative(self):
        self.rocket.set_engine_state(False)


class RotationListener(StateListener):
    def __init__(self, rocket, cw_key, ccw_key):
        super().__init__()
        self.rocket = rocket
        self.cw_key = cw_key
        self.ccw_key = ccw_key
        self.direction = 0

    def state_occurred(self):
        self.direction = 0
        pressed = pygame.key.get_pressed()
        if pressed[self.cw_key]:
            self.direction += 1
        elif pressed[self.ccw_key]:
            self.direction -= 1
        return self.direction != 0

    def perform_action(self):
        self.rocket.set_rotation(self.direction)

    def perform_alternative(self):
        self.rocket.set_rotation(0)


class ShootListener(EventListener):
    def __init__(self, rocket, key):
        super().__init__()
        self.rocket = rocket
        self.key = key

    def has_found(self, event):
        return event.type == pygame.KEYDOWN and event.key == self.key

    def perform_action(self):
        self.rocket.shoot()

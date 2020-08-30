import pygame


class Rocket:
    def __init__(self, pos, angle, color):
        self.pos = pos
        self.angle = angle
        self.color = color

    def draw(self, window):
        pygame.draw.polygon(window, self.color, self.get_polygon())

    def get_polygon(self):
        return [(50, 50), (50, 100), (100, 50)]

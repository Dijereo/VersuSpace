import pygame

from colors import *


class Text:
    def __init__(self, font_name, font_size, text, color, center):
        font = pygame.font.SysFont(font_name, font_size)
        self.text_surface = font.render(text, True, color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = center

    def draw(self, window):
        window.blit(self.text_surface, self.text_rect)


class Button:
    BORDER_SIZE = 10

    def __init__(self, font_name, font_size, text, color, rect):
        self.color = color
        self.default_text = Text(font_name, font_size, text, color, rect.center)
        self.hover_text = Text(font_name, font_size, text, Colors.BLACK, rect.center)
        self.rect = rect
        self.inner_rect = self.rect.inflate(-Button.BORDER_SIZE, -Button.BORDER_SIZE)
        self.hovered = False

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        if self.hovered:
            self.hover_text.draw(window)
        else:
            pygame.draw.rect(window, Colors.BLACK, self.inner_rect)
            self.default_text.draw(window)

    def is_hovered(self, x, y):
        return self.rect.collidepoint(x, y)

    def set_hovered(self, hovered):
        self.hovered = hovered

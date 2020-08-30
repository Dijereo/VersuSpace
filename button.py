import pygame

from colors import *


class Button:
    BORDER_SIZE = 10

    def __init__(self, font_name, font_size, text, color, rect):
        font = pygame.font.SysFont(font_name, font_size)
        self.color = color
        self.text_surface = font.render(text, True, self.color)
        self.hover_text_surface = font.render(text, True, Colors.BLACK)
        self.rect = rect
        self.inner_rect = self.rect.inflate(-Button.BORDER_SIZE, -Button.BORDER_SIZE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.rect.center
        self.hovered = False

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        if self.hovered:
            window.blit(self.hover_text_surface, self.text_rect)
        else:
            pygame.draw.rect(window, Colors.BLACK, self.inner_rect)
            window.blit(self.text_surface, self.text_rect)

    def is_hovered(self, x, y):
        return self.rect.collidepoint(x, y)

    def set_hovered(self, hovered):
        self.hovered = hovered

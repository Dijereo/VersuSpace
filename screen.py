from button import *
from colors import *
from event import *


class Screen:
    def __init__(self, app):
        self.width = app.width
        self.height = app.height
        self.handler = EventHandler()
        self.handler.add_event_listeners([app.quit_listener])

    def step(self, time):
        pass

    def draw(self, window):
        raise NotImplementedError('Screen class draw method is abstract')


class ScreenWithButtons(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.buttons = {}
        for name, button, onclick in self.construct_buttons(app):
            self.buttons[name] = button
            self.handler.add_event_listeners([ButtonClickListener(button, onclick)])
            self.handler.add_state_listeners([ButtonHoverListener(button)])

    def construct_buttons(self, app):
        raise NotImplementedError('ScreenWithButtons construct_buttons method is abstract')

    def draw(self, window):
        for button in self.buttons.values():
            button.draw(window)


class MenuScreen(ScreenWithButtons):
    def __init__(self, app):
        super().__init__(app)

    def construct_buttons(self, app):
        return [('play', Button('Consolas', 30, 'Play', Colors.GREEN,
                                pygame.Rect(app.width // 4, app.height // 7,
                                            app.width // 2, app.height // 7)),
                 app.start_game),
                ('help', Button('Consolas', 30, 'Help', Colors.YELLOW,
                                pygame.Rect(app.width // 4, 3 * app.height // 7,
                                            app.width // 2, app.height // 7)),
                 app.display_instructions),
                ('exit', Button('Consolas', 30, 'Exit', Colors.RED,
                                pygame.Rect(app.width // 4, 5 * app.height // 7,
                                            app.width // 2, app.height // 7)),
                 app.stop)]

    def draw(self, window):
        window.fill(Colors.BLACK)
        super().draw(window)


class ComingSoonScreen(ScreenWithButtons):
    def __init__(self, app):
        super().__init__(app)
        font = pygame.font.SysFont('Consolas', 75)
        self.text_surface = font.render('Coming Soon', True, Colors.GREEN)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (app.width // 2, app.height // 2)

    def construct_buttons(self, app):
        return [('back', Button('Consolas', 30, 'Back', Colors.ORANGE,
                                pygame.Rect(3 * app.width // 4, 6 * app.height // 7,
                                            app.width // 4, app.height // 7)),
                 app.display_menu)]

    def draw(self, window):
        window.fill(Colors.BLACK)
        super().draw(window)
        window.blit(self.text_surface, self.text_rect)


class InstructionScreen(ScreenWithButtons):
    def __init__(self, app):
        super().__init__(app)
        font = pygame.font.SysFont('Consolas', 20)
        self.text_surface1 = font.render('Use "A", "W", "D" to move and "E" to shoot', True, Colors.BLUE)
        self.text_rect1 = self.text_surface1.get_rect()
        self.text_rect1.center = (app.width // 2, 40)
        self.text_surface2 = font.render('Use arrow keys to move and "/" to shoot', True, Colors.RED)
        self.text_rect2 = self.text_surface2.get_rect()
        self.text_rect2.center = (app.width // 2, 80)
        self.text_surface3 = font.render('While playing press "Q" to exit', True, Colors.YELLOW)
        self.text_rect3 = self.text_surface3.get_rect()
        self.text_rect3.center = (app.width // 2, 120)

    def construct_buttons(self, app):
        return [('back', Button('Consolas', 30, 'Back', Colors.ORANGE,
                                pygame.Rect(3 * app.width // 4, 6 * app.height // 7,
                                            app.width // 4, app.height // 7)),
                 app.display_menu)]

    def draw(self, window):
        window.fill(Colors.BLACK)
        super().draw(window)
        window.blit(self.text_surface1, self.text_rect1)
        window.blit(self.text_surface2, self.text_rect2)
        window.blit(self.text_surface3, self.text_rect3)

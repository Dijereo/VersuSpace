from button import *
from colors import *
from event import *


class Screen:
    def __init__(self, app):
        self.handler = EventHandler()
        self.handler.add_event_listeners([app.quit_listener])

    def draw(self, window):
        raise NotImplementedError('Screen class draw method is abstract')


class MenuScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.play_button = Button(
            'Consolas', 30, 'Play', Colors.GREEN, pygame.Rect(
                app.width // 4, app.height // 7, app.width // 2, app.height // 7))
        self.help_button = Button(
            'Consolas', 30, 'Help', Colors.YELLOW, pygame.Rect(
                app.width // 4, 3 * app.height // 7, app.width // 2, app.height // 7))
        self.exit_button = Button(
            'Consolas', 30, 'Exit', Colors.RED, pygame.Rect(
                app.width // 4, 5 * app.height // 7, app.width // 2, app.height // 7))
        self.handler.add_event_listeners([
            ButtonClickListener(self.play_button, app.start_game),
            ButtonClickListener(self.help_button, app.display_coming_soon),
            ButtonClickListener(self.exit_button, app.stop)])
        self.handler.add_state_listeners([
            ButtonHoverListener(self.play_button),
            ButtonHoverListener(self.help_button),
            ButtonHoverListener(self.exit_button)])

    def draw(self, window):
        window.fill(Colors.BLACK)
        self.play_button.draw(window)
        self.help_button.draw(window)
        self.exit_button.draw(window)


class ComingSoonScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        font = pygame.font.SysFont('Consolas', 75)
        self.text_surface = font.render('Coming Soon', True, Colors.GREEN)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (app.width // 2, app.height // 2)
        self.back_button = Button(
            'Consolas', 30, 'Back', Colors.ORANGE, pygame.Rect(
                3 * app.width // 4, 6 * app.height // 7, app.width // 4, app.height // 7))
        self.handler.add_event_listeners([
            ButtonClickListener(self.back_button, app.display_menu)])
        self.handler.add_state_listeners([
            ButtonHoverListener(self.back_button)])

    def draw(self, window):
        window.fill(Colors.BLACK)
        self.back_button.draw(window)
        window.blit(self.text_surface, self.text_rect)

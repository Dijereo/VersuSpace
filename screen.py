from button import *
from colors import *
from event import *


class Screen:
    def __init__(self, app):
        self.handler = EventHandler()
        self.handler.add_event_listeners([app.quit_listener])

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


class ComingSoonScreen(ScreenWithButtons):
    def __init__(self, app):
        super().__init__(app)
        font = pygame.font.SysFont('Consolas', 75)
        self.text_surface = font.render('Coming Soon', True, Colors.GREEN)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (app.width // 2, app.height // 2)

    def construct_buttons(self, app):
        return [('back',
                 Button('Consolas', 30, 'Back', Colors.ORANGE, pygame.Rect(
                     3 * app.width // 4, 6 * app.height // 7,
                     app.width // 4, app.height // 7)),
                 app.display_menu)]

    def draw(self, window):
        window.fill(Colors.BLACK)
        super().draw(window)
        window.blit(self.text_surface, self.text_rect)

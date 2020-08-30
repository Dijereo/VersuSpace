from button import *
from colors import *
from event import *


class App:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('VersuSpace')
        self.running = True
        self.quit_listener = AppQuitListener(self)
        self.menu_screen = MenuScreen(self)
        self.coming_soon_screen = ComingSoonScreen(self)
        self.current_screen = self.menu_screen

    def run(self):
        while self.running:
            self.send_events_to()
            self.current_screen.draw(self.window)
            pygame.display.update()

    def send_events_to(self):
        for event in pygame.event.get():
            self.current_screen.handler.handle(event)

    def stop(self):
        self.running = False

    def display_coming_soon(self):
        self.current_screen = self.coming_soon_screen

    def display_menu(self):
        self.current_screen = self.menu_screen


class Screen:
    def __init__(self, app):
        self.handler = EventHandler([app.quit_listener])

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
        self.handler.add_listeners([
            ButtonClickListener(self.play_button, app.display_coming_soon),
            ButtonClickListener(self.help_button, app.display_coming_soon),
            ButtonClickListener(self.exit_button, app.stop)])

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
        self.handler.add_listeners([
            ButtonClickListener(self.back_button, app.display_menu)])

    def draw(self, window):
        window.fill(Colors.BLACK)
        self.back_button.draw(window)
        window.blit(self.text_surface, self.text_rect)

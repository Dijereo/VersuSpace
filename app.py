from game_screen import *


class App:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('VersuSpace')
        self.running = True
        self.quit_listener = AppQuitListener(self)
        self.menu_screen = MenuScreen(self)
        self.game_screen = GameScreen(self)
        self.coming_soon_screen = ComingSoonScreen(self)
        self.current_screen = self.menu_screen

    def run(self):
        while self.running:
            self.current_screen.handler.handle_events()
            self.current_screen.draw(self.window)
            pygame.display.update()

    def stop(self):
        self.running = False

    def display_coming_soon(self):
        self.current_screen = self.coming_soon_screen

    def display_menu(self):
        self.current_screen = self.menu_screen

    def start_game(self):
        self.current_screen = self.game_screen

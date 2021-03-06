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
        self.instruction_screen = InstructionScreen(self)
        self.current_screen = self.menu_screen
        self.clock = pygame.time.Clock()
        self.fps = 60

    def run(self):
        while self.running:
            self.current_screen.handler.handle_events()
            self.current_screen.step(1 / self.fps)
            self.current_screen.draw(self.window)
            pygame.display.update()
            self.clock.tick(self.fps)

    def stop(self):
        self.running = False

    def display_coming_soon(self):
        self.current_screen = self.coming_soon_screen

    def display_menu(self):
        self.current_screen = self.menu_screen

    def display_instructions(self):
        self.current_screen = self.instruction_screen

    def start_game(self):
        self.current_screen = self.game_screen

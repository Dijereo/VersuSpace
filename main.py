import pygame


class Button:
    BORDER_SIZE = 5

    def __init__(self, font_name, font_size, text, color, rect):
        font = pygame.font.SysFont(font_name, font_size)
        self.color = color
        self.text_surface = font.render(text, True, self.color)
        self.rect = rect
        self.inner_rect = self.rect.inflate(-Button.BORDER_SIZE, -Button.BORDER_SIZE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.rect.center

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        pygame.draw.rect(window, (0, 0, 0), self.inner_rect)
        window.blit(self.text_surface, self.text_rect)


class Screen:
    def draw(self, window):
        raise NotImplementedError('Screen class draw method is abstract')


class MenuScreen(Screen):
    def draw(self, window):
        button = Button('Consolas', 30, 'Hello', (0, 255, 0), pygame.Rect(50, 50, 200, 50))
        window.fill((0, 0, 100))
        button.draw(window)


class GameScreen(Screen):
    def draw(self, window):
        window.fill((0, 100, 0))


class EventQueue:
    def send_events_to(self, handler):
        for event in pygame.event.get():
            handler.handle(event)


class EventHandler:
    def __init__(self, listeners):
        self.listeners = listeners
        
    def handle(self, event):
        for listener in self.listeners:
            if listener.has_found(event):
                listener.perform_action()


class EventListener:
    def has_found(self, event):
        raise NotImplementedError('EventListener class hasFound method is abstract')

    def perform_action(self):
        raise NotImplementedError('EventListener class performAction method is abstract')


class AppQuitListener(EventListener):
    def __init__(self, app):
        self.app = app

    def has_found(self, event):
        return event.type == pygame.QUIT

    def perform_action(self):
        self.app.stop()


class StartGameListener(EventListener):
    def __init__(self, app):
        self.app = app
        
    def has_found(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN

    def perform_action(self):
        self.app.start_game()


class App:
    def __init__(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('VersuSpace')
        self.menu_screen = MenuScreen()
        self.game_screen = GameScreen()
        self.current_screen = self.menu_screen
        self.quit_listener = AppQuitListener(self)
        self.start_game_listener = StartGameListener(self)
        self.queue = EventQueue()
        self.handler = EventHandler([self.quit_listener, self.start_game_listener])
        self.running = True

    def run(self):
        while self.running:
            self.queue.send_events_to(self.handler)
            self.current_screen.draw(self.window)
            pygame.display.update()

    def stop(self):
        self.running = False

    def start_game(self):
        self.current_screen = self.game_screen


def main():
    pygame.init()
    pygame.font.init()
    app = App()
    app.run()
    pygame.quit()


if __name__ == '__main__':
    main()

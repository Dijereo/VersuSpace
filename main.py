import pygame


class Button:
    def draw(self, window):
        font = pygame.font.SysFont('Consolas', 30)
        text_surface = font.render('Some Text', False, (0, 0, 0))
        window.blit(text_surface, (0, 0))


class Screen:
    def draw(self, window):
        raise NotImplementedError('Screen class draw method is abstract')


class MenuScreen(Screen):
    def draw(self, window):
        button = Button()
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

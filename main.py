import pygame


class Colors:
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)


class Button:
    BORDER_SIZE = 5

    def __init__(self, font_name, font_size, text, color, rect):
        font = pygame.font.SysFont(font_name, font_size)
        self.color = color
        self.text_surface = font.render(text, True, self.color)
        self.hover_text_surface = font.render(text, True, Colors.BLACK)
        self.rect = rect
        self.inner_rect = self.rect.inflate(-Button.BORDER_SIZE, -Button.BORDER_SIZE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = self.rect.center

    def is_hovered(self):
        return self.rect.collidepoint(*pygame.mouse.get_pos())

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        if self.is_hovered():
            window.blit(self.hover_text_surface, self.text_rect)
        else:
            pygame.draw.rect(window, Colors.BLACK, self.inner_rect)
            window.blit(self.text_surface, self.text_rect)


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
                app.width // 4, app.height // 5, app.width // 2, app.height // 5))
        self.exit_button = Button(
            'Consolas', 30, 'Exit', Colors.RED, pygame.Rect(
                app.width // 4, 3 * app.height // 5, app.width // 2, app.height // 5))
        self.handler.add_listeners([
            ButtonClickListener(self.play_button, app.start_game),
            ButtonClickListener(self.exit_button, app.stop)])

    def draw(self, window):
        window.fill(Colors.BLACK)
        self.play_button.draw(window)
        self.exit_button.draw(window)


class GameScreen(Screen):
    def __init__(self, app):
        super().__init__(app)

    def draw(self, window):
        window.fill(Colors.BLACK)


class EventHandler:
    def __init__(self, listeners):
        self.listeners = listeners

    def add_listeners(self, listeners):
        self.listeners += listeners
        
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


class ButtonClickListener(EventListener):
    def __init__(self, button, onclick):
        self.button = button
        self.onclick = onclick

    def has_found(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.button.is_hovered()

    def perform_action(self):
        self.onclick()


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

    def start_game(self):
        self.current_screen = self.game_screen


def main():
    pygame.init()
    app = App(500, 500)
    app.run()
    pygame.quit()


if __name__ == '__main__':
    main()

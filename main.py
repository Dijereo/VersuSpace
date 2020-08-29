import pygame


class Button:
    BORDER_SIZE = 5

    def __init__(self, font_name, font_size, text, color, rect):
        font = pygame.font.SysFont(font_name, font_size)
        self.color = color
        self.text_surface = font.render(text, True, self.color)
        self.hover_text_surface = font.render(text, True, (0, 0, 0))
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
            pygame.draw.rect(window, (0, 0, 0), self.inner_rect)
            window.blit(self.text_surface, self.text_rect)


class Screen:
    def __init__(self, app):
        self.handler = EventHandler([app.quit_listener])

    def draw(self, window):
        raise NotImplementedError('Screen class draw method is abstract')


class MenuScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.button = Button('Consolas', 30, 'Hello', (0, 255, 0), pygame.Rect(50, 50, 200, 50))
        self.handler.add_listeners([
            ButtonHoverListener(self.button),
            ButtonClickListener(self.button, app.start_game)
        ])

    def draw(self, window):
        window.fill((0, 0, 100))
        self.button.draw(window)


class GameScreen(Screen):
    def __init__(self, app):
        super().__init__(app)

    def draw(self, window):
        window.fill((0, 100, 0))


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


class ButtonHoverListener(EventListener):
    def __init__(self, button):
        self.button = button

    def has_found(self, event):
        return True

    def perform_action(self):
        self.button.hovered = self.button.rect.collidepoint(*pygame.mouse.get_pos())


class ButtonClickListener(EventListener):
    def __init__(self, button, onclick):
        self.button = button
        self.onclick = onclick

    def has_found(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN
                and self.button.rect.collidepoint(event.pos))

    def perform_action(self):
        self.onclick()


class App:
    def __init__(self):
        self.window = pygame.display.set_mode((500, 500))
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
    pygame.font.init()
    app = App()
    app.run()
    pygame.quit()


if __name__ == '__main__':
    main()

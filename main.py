import pygame


class Screen:
    def draw(self, window):
        raise NotImplementedError('Screen class draw method is abstract')


class MenuScreen(Screen):
    def draw(self, window):
        window.fill((0, 0, 100))


class GameScreen(Screen):
    def draw(self, window):
        window.fill((0, 100, 0))


class EventQueue:
    def sendEventsTo(self, handler):
        for event in pygame.event.get():
            handler.handle(event)


class EventHandler:
    def __init__(self, app):
        self.app = app
        
    def handle(self, event):
        if event.type == pygame.QUIT:
            self.app.stop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.app.startGame()


class App:
    def __init__(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('VersuSpace')
        self.menuscreen = MenuScreen()
        self.gamescreen = GameScreen()
        self.currentscreen = self.menuscreen
        self.queue = EventQueue()
        self.handler = EventHandler(self)
        self.running = True

    def run(self):
        while self.running:
            self.queue.sendEventsTo(self.handler)
            self.currentscreen.draw(self.window)
            pygame.display.update()

    def stop(self):
        self.running = False

    def startGame(self):
        self.currentscreen = self.gamescreen


def main():
    pygame.init()
    app = App()
    app.run()
    pygame.quit()


if __name__ == '__main__':
    main()

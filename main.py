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
    def __init__(self, app, listeners):
        self.app = app
        self.listeners = listeners
        
    def handle(self, event):
        for listener in self.listeners:
            if listener.hasFound(event):
                listener.performAction()


class EventListener:
    def hasFound(self, event):
        raise NotImplementedError('EventListener class hasFound method is abstract')

    def performAction(self):
        raise NotImplementedError('EventListener class performAction method is abstract')


class AppQuitListener(EventListener):
    def __init__(self, app):
        self.app = app

    def hasFound(self, event):
        return event.type == pygame.QUIT

    def performAction(self):
        self.app.stop()


class StartGameListener(EventListener):
    def __init__(self, app):
        self.app = app
        
    def hasFound(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN

    def performAction(self):
        self.app.startGame()


class App:
    def __init__(self):
        self.setupWindow()
        self.setupScreens()
        self.setupEvents()
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

    def setupWindow(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('VersuSpace')

    def setupScreens(self):
        self.menuscreen = MenuScreen()
        self.gamescreen = GameScreen()
        self.currentscreen = self.menuscreen

    def setupEvents(self):
        self.quitlistener = AppQuitListener(self)
        self.startgamelistener = StartGameListener(self)
        self.queue = EventQueue()
        self.handler = EventHandler(self, [self.quitlistener, self.startgamelistener])


def main():
    pygame.init()
    app = App()
    app.run()
    pygame.quit()


if __name__ == '__main__':
    main()

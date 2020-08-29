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


class App:
    def __init__(self):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('VersuSpace')
        self.menuscreen = MenuScreen()
        self.gamescreen = GameScreen()
        self.currentscreen = self.menuscreen
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.currentscreen = self.gamescreen
            self.currentscreen.draw(self.window)
            pygame.display.update()


def main():
    pygame.init()
    app = App()
    app.run()
    pygame.quit()


if __name__ == '__main__':
    main()

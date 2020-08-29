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


def main():
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('VersuSpace')
    menuscreen = MenuScreen()
    gamescreen = GameScreen()
    currentscreen = menuscreen
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                currentscreen = gamescreen
        currentscreen.draw(window)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()

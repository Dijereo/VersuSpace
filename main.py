import pygame


class Screen:
    def draw(self, window):
        raise NotImplementedError('Screen class draw method is abstract')


class MenuScreen(Screen):
    def draw(self, window):
        window.fill((0, 0, 100))


def main():
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('VersuSpace')
    menuscreen = MenuScreen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        menuscreen.draw(window)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()

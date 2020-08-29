import pygame


def main():
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('VersuSpace')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()

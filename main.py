from app import *


def main():
    pygame.init()
    app = App(500, 500)
    app.run()
    pygame.quit()


if __name__ == '__main__':
    main()

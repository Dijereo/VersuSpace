from button import *
from colors import *
from event import *


class Screen:
    def __init__(self, app):
        self.width = app.width
        self.height = app.height
        self.handler = EventHandler()
        self.handler.add_event_listeners([app.quit_listener])

    def step(self, time):
        pass

    def draw(self, window):
        raise NotImplementedError('Screen class draw method is abstract')


class ScreenWithButtons(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.buttons = {}
        for name, button, onclick in self.construct_buttons(app):
            self.buttons[name] = button
            self.handler.add_event_listeners([ButtonClickListener(button, onclick)])
            self.handler.add_state_listeners([ButtonHoverListener(button)])

    def construct_buttons(self, app):
        raise NotImplementedError('ScreenWithButtons construct_buttons method is abstract')

    def draw(self, window):
        for button in self.buttons.values():
            button.draw(window)


class MenuScreen(ScreenWithButtons):
    def __init__(self, app):
        super().__init__(app)

    def construct_buttons(self, app):
        return [('play', Button('Consolas', 30, 'Play', Colors.GREEN,
                                pygame.Rect(app.width // 4, app.height // 7,
                                            app.width // 2, app.height // 7)),
                 app.start_game),
                ('help', Button('Consolas', 30, 'Help', Colors.YELLOW,
                                pygame.Rect(app.width // 4, 3 * app.height // 7,
                                            app.width // 2, app.height // 7)),
                 app.display_instructions),
                ('exit', Button('Consolas', 30, 'Exit', Colors.RED,
                                pygame.Rect(app.width // 4, 5 * app.height // 7,
                                            app.width // 2, app.height // 7)),
                 app.stop)]

    def draw(self, window):
        window.fill(Colors.BLACK)
        super().draw(window)


class ComingSoonScreen(ScreenWithButtons):
    def __init__(self, app):
        super().__init__(app)
        self.text = Text('Consolas', 75, 'Coming Soon', Colors.GREEN, (app.width // 2, app.height // 2))

    def construct_buttons(self, app):
        return [('back', Button('Consolas', 30, 'Back', Colors.ORANGE,
                                pygame.Rect(3 * app.width // 4, 6 * app.height // 7,
                                            app.width // 4, app.height // 7)),
                 app.display_menu)]

    def draw(self, window):
        window.fill(Colors.BLACK)
        super().draw(window)
        self.text.draw(window)


class InstructionScreen(ScreenWithButtons):
    def __init__(self, app):
        super().__init__(app)
        self.text1 = Text('Consolas', 20, 'Use "A", "W", "D" to move and "E" to shoot', Colors.BLUE, (app.width // 2, 40))
        self.text2 = Text('Consolas', 20, 'Use arrow keys to move and "/" to shoot', Colors.RED, (app.width // 2, 80))
        self.text3 = Text('Consolas', 20, 'While playing press "Q" to exit', Colors.YELLOW, (app.width // 2, 120))

    def construct_buttons(self, app):
        return [('back', Button('Consolas', 30, 'Back', Colors.ORANGE,
                                pygame.Rect(3 * app.width // 4, 6 * app.height // 7,
                                            app.width // 4, app.height // 7)),
                 app.display_menu)]

    def draw(self, window):
        window.fill(Colors.BLACK)
        super().draw(window)
        self.text1.draw(window)
        self.text2.draw(window)
        self.text3.draw(window)

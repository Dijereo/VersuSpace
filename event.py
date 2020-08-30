import pygame


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
        return (event.type == pygame.MOUSEBUTTONDOWN
                and self.button.is_hovered(*pygame.mouse.get_pos()))

    def perform_action(self):
        self.onclick()


class KeyPressedListener(EventListener):
    def __init__(self, key):
        self.key = key

    def has_found(self, event):
        return pygame.key.get_pressed()[self.key]


class StateListener:
    def state_occurred(self):
        raise NotImplementedError('StateListener state_occurred method is abstract')

    def perform_action(self):
        raise NotImplementedError('StateListener perform_action method is abstract')

    def perform_alternative(self):
        raise NotImplementedError('StateListener perform_default method is abstract')


class ButtonHoverListener(StateListener):
    def __init__(self, button):
        self.button = button

    def state_occurred(self):
        return self.button.is_hovered(*pygame.mouse.get_pos())

    def perform_action(self):
        self.button.set_hovered(True)

    def perform_alternative(self):
        self.button.set_hovered(False)

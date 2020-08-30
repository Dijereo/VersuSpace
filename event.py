import pygame


class EventHandler:
    def __init__(self):
        self.event_listeners = []
        self.state_listeners = []

    def add_event_listeners(self, listeners):
        self.event_listeners += listeners

    def add_state_listeners(self, listeners):
        self.state_listeners += listeners

    def handle_events(self):
        for listener in self.state_listeners:
            if listener.state_occurred():
                listener.perform_action()
            else:
                listener.perform_alternative()
        for event in pygame.event.get():
            for listener in self.event_listeners:
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


class StateListener:
    def state_occurred(self):
        raise NotImplementedError('StateListener state_occurred method is abstract')

    def perform_action(self):
        raise NotImplementedError('StateListener perform_action method is abstract')

    def perform_alternative(self):
        raise NotImplementedError('StateListener perform_default method is abstract')


class KeyPressedListener(StateListener):
    def __init__(self, key):
        self.key = key

    def state_occurred(self):
        return pygame.key.get_pressed()[self.key]


class ButtonHoverListener(StateListener):
    def __init__(self, button):
        self.button = button

    def state_occurred(self):
        return self.button.is_hovered(*pygame.mouse.get_pos())

    def perform_action(self):
        self.button.set_hovered(True)

    def perform_alternative(self):
        self.button.set_hovered(False)

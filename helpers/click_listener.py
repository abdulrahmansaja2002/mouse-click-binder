from pynput.mouse import Listener

class ClickBinder:
    def __init__(self):
        self.listener = Listener(on_click=self.on_click)
        self.key_bindings = {}

    def on_click(self, x, y, button, pressed):
        # print(f"{x} {y} {button} {pressed}")
        button_action = self.key_bindings.get(button)
        if button_action and pressed:
            button_action()

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

    def bind(self, key, action):
        self.key_bindings[key] = action

    def unbind(self, key):
        self.key_bindings.pop(key, None)
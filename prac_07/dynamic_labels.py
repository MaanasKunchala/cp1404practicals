from kivy.app import App
from kivy.app import Builder


class DynamicLabels(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        names = ["Cat", "Dog", "Dinosaur"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_widgets.kv')
        return self.root


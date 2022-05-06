from kivy.app import App
from kivy.app import Builder


class ConvertMilesToKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):


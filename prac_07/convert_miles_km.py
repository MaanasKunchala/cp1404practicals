from kivy.app import App
from kivy.app import Builder

MILE_TO_KILOMETER = 1.61


class ConvertMilesToKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        try:
            result = float(value) * MILE_TO_KILOMETER
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, value, increment):
        try:
            result = float(value) + increment
            self.root.ids.input_number.text = str(result)
            self.handle_conversion(result)
        except ValueError:
            result = 0 + increment
            self.root.ids.input_number.text = str(result)
            self.handle_conversion(result)


ConvertMilesToKm().run()


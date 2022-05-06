from kivy.app import App
from kivy.app import Builder


class ConvertMilesToKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        try:
            result = float(value) * 1.61
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, value, increment):
        result = float(value) + increment
        self.root.ids.input_number.text = str(result)


ConvertMilesToKm().run()


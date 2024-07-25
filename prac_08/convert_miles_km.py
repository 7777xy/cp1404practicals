from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_TO_KM = 1.60934


class MilesConversion(App):
    """MilesConversion is a Kivy App for converting miles to kilometres."""
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Type in the field & press convert"
        return self.root


MilesConversion().run()

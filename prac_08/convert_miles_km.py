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

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.message = self.get_valid_mile()

    def get_valid_mile(self):
        """Get a valid mile and if not valid, 0 will occur."""
        try:
            mile = float(self.root.ids.user_input.text)
            return mile
        except ValueError:
            return 0


MilesConversion().run()

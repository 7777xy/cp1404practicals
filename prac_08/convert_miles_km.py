from kivy.app import App
from kivy.properties import StringProperty

MILE_TO_KM = 1.60934


class MilesConversion(App):
    """MilesConversion is a Kivy App for converting miles to kilometres."""
    message = StringProperty()


MilesConversion().run()

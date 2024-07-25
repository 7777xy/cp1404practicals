from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (250, 150)
        self.title = 'Square Number 2'
        self.root = Builder.load_file('squaring.kv')
        return self.root


SquareNumberApp().run()

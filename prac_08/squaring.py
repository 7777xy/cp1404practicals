from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class Squaring(App):
    """Squaring is a Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (250, 150)
        self.title = 'Square Number 2'
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call), output result to label widget."""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


Squaring().run()

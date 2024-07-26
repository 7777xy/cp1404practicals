from kivy.app import App
from kivy.lang import Builder

BLANK_STRING = ''


class BoxLayoutDemo(App):
    """Box Layout Demo is a Kivy App for greet people."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = 'Box Layout Demo'
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greeting, output result to label widget."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle to reset both text field and output label to blank."""
        self.root.ids.output_label.text = BLANK_STRING
        self.root.ids.input_name.text = BLANK_STRING


BoxLayoutDemo().run()

from kivy.app import App


class DynamicLabels(App):
    """Main program - Kivy app to dynamic labels creation."""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]


DynamicLabels().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.theming import ThemeManager

Builder.load_file('ejemplos/tentry.kv')

class Example(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'BlueGray'

    def build(self):
        return Factory.Example()

    def show_password(self, field, button):
        """
        Called when you press the right button in the password field
        for the screen TextFields.

        instance_field: kivy.uix.textinput.TextInput;
        instance_button: kivymd.button.MDIconButton;

        """

        # Show or hide text of password, set focus field
        # and set icon of right button.
        field.password = not field.password
        field.focus = True
        button.icon = 'eye' if button.icon == 'eye-off' else 'eye-off'


if __name__ == '__main__':
    Example().run()
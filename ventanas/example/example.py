from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast

root_kv = """
#:import NavigationLayout kivymd.uix.navigationdrawer.NavigationLayout


<ContentNavigationDrawer@MDNavigationDrawer>:
    drawer_logo: "demos/kitchen_sink/assets/drawer_logo.png"

    NavigationDrawerSubheader:
        text: "Menu:"

    NavigationDrawerIconButton:
        icon: "numeric-1-circle"
        text: "First menu button"
        on_release: app.callback(self.text)

    NavigationDrawerIconButton:
        icon: "checkbox-blank-circle"
        text: "Second menu button"
        on_release: app.callback(self.text)

    NavigationDrawerIconButton:
        icon: "numeric-3-box"
        text: "Third menu button"
        on_release: app.callback(self.text)


NavigationLayout:
    id: nav_layout

    ContentNavigationDrawer:
        id: nav_drawer

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            id: toolbar
            title: app.title
            md_bg_color: app.theme_cls.primary_color
            background_palette: "Primary"
            background_hue: "500"
            elevation: 10
            left_action_items:
                [["menu", lambda x: app.root.toggle_nav_drawer()]]

        BoxLayout:
            id: content
            orientation: "vertical"
"""


class abc(MDApp):
    def __init__(self, **kwargs):
        self.title = "KivyMD Example - Navigation Drawer"
        self.theme_cls.primary_palette = "Teal"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(root_kv)

    def callback(self, text):
        toast(f'Pressed item menu "{text}"')


if __name__ == "__main__":
    abc().run()
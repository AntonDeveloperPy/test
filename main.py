from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivymd.uix.hero import MDHeroFrom
from kivymd.uix.snackbar import Snackbar

KV = '''

<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:


    MDBottomNavigation:
        selected_color_background: "orange"
        text_color_active: "lightgrey"
        

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Mail'
            MDGridLayout:
                rows:2
                MDCard:
                    orientation: "vertical"
                    MDRaisedButton:
                        text: "Set theme"




        MDBottomNavigationItem:
            name: 'screen 2'
            text: ''
            MDTextField:
                id: text_field_error
                hint_text: "Helper text on error (press 'Enter')"
                helper_text: "There will always be a mistake"
                helper_text_mode: "on_error"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint_x: .5

        MDBottomNavigationItem:
            name: 'screen 3'
            text: ''








    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "black"
                    specific_text_color: "white"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Header title"
                    text: "Header text"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    MDRaisedButton:
                        text: "Set theme"
                        on_press: app.switch_theme_style()



'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(KV)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.screen.ids.text_field_error.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        return self.screen

    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def set_error_message(self, instance_textfield):
        if 'd':
            print('d')


Test().run()

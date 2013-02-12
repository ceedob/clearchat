from kivy.app import App
from kivy.uix.widget import Widget


class ClearChat(Widget):
    pass


class ClearChatApp(App):
    def build(self):
        return ClearChat()


if __name__ == '__main__':
    ClearChatApp().run()
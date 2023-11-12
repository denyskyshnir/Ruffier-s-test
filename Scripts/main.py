import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

# Fix OpenGL 2.0 bug
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class BaseScreen(Screen):
    def __init__(self, screen_name, next_screen_name, button_text, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.screen_name = screen_name
        self.next_screen_name = next_screen_name
        self.button_text = button_text

        label = Label(text=f'Ти на {self.screen_name} екрані')
        button = Button(text=self.button_text, size_hint=(0.25, 0.15), pos=(300, 10))
        button.bind(on_press=self.go_to_next)

        self.add_widget(label)
        self.add_widget(button)

    def go_to_next(self, instance):
        self.manager.current = self.next_screen_name


class FirstScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__('Screen 1', 'Screen 2',
                                          'Почати', **kwargs)


class SecondScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__('Screen 2', 'Screen 3',
                                           'Продовжити', **kwargs)


class ThirdScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__('Screen 3', 'Screen 4',
                                          'Продовжити', **kwargs)


class FourthScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(FourthScreen, self).__init__('Screen 4', 'Screen 5',
                                           'Завершити', **kwargs)


class FivethScreen(Screen):
    def build(self):
        label = Label(text='Screen 5')
        self.add_widget(label)


class MyApp(App):
    def build(self):
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '600')

        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='Screen 1'))
        sm.add_widget(SecondScreen(name='Screen 2'))
        sm.add_widget(ThirdScreen(name='Screen 3'))
        sm.add_widget(FourthScreen(name='Screen 4'))
        sm.add_widget(FivethScreen(name='Screen 5'))
        return sm


if __name__ == '__main__':
    MyApp().run()  # Запуск додатку Kivy

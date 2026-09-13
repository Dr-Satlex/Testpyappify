from kivy.app import App
from kivy.uix.label import Label

class AtomicTest(App):
    def build(self):
        return Label(text="Piappify Build Environment Works!")

if __name__ == '__main__':
    AtomicTest().run()

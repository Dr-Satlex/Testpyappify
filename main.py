"""
Minimal Kivy app used to smoke-test the Piappify build pipeline.

Piappify clones this repo, patches buildozer.spec (title/package.name/
package.domain), then runs `buildozer -v android debug`. If this builds
and installs cleanly, the pipeline itself is healthy.
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=40, spacing=20, **kwargs)
        self.label = Label(
            text="Hello from Piappify!\nIf you can see this, the build pipeline works.",
            font_size=22,
            halign="center",
        )
        self.counter = 0
        self.button = Button(text="Tap me", font_size=20, size_hint=(1, 0.3))
        self.button.bind(on_press=self.on_tap)
        self.add_widget(self.label)
        self.add_widget(self.button)

    def on_tap(self, instance):
        self.counter += 1
        self.button.text = f"Tapped {self.counter} time{'s' if self.counter != 1 else ''}"


class PiappifyTestApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    PiappifyTestApp().run()

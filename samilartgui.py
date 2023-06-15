from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
from samila import GenerativeImage, Projection
import random
import math
import uuid
import os

class MyApp(App):
    def build(self):
        Config.set('graphics', 'resizable', '0')
        Window.size = (720, 480)
        Window.minimum_width = 720
        Window.minimum_height = 480
        Window.maximum_width = 720
        Window.maximum_height = 480
        self.title = 'SamilaRT - GUI'
        layout = GridLayout(cols=1, spacing=10, padding=10, size=(720, 480))

        self.label = Label(text='', size_hint=(None, None), size=(180, 50))
        Clock.schedule_once(lambda dt: self.start_typing_animation(), 1)

        self.image_widget = Image()
        button_layout = GridLayout(cols=3, spacing=10, size_hint=(None, None), size=(500, 50))

        self.button = Button(text='Generate and Plot', background_color=(0, 1, 0, 1))
        self.seed_input = TextInput(text='', hint_text='Enter seed (enter random number)')
        self.projection_spinner = Spinner(
            text='Select projection',
            values=['Rectilinear', 'Polar', 'Aitoff', 'Hammer', 'Lambert', 'Mollweide']
        )
        self.button.bind(on_press=self.generate_and_plot)

        button_layout.add_widget(self.seed_input)
        button_layout.add_widget(self.projection_spinner)
        button_layout.add_widget(self.button)

        layout.add_widget(self.label)
        layout.add_widget(self.image_widget)
        layout.add_widget(button_layout)

        return layout

    def start_typing_animation(self):
        text = "Created by Gerry Auditya"
        typing_speed = 0.10
        typing_index = 0

        def update_label_text(dt):
            nonlocal typing_index
            if typing_index <= len(text):
                self.label.text = text[:typing_index]
                typing_index += 1
                Clock.schedule_once(update_label_text, typing_speed)

        Clock.schedule_once(update_label_text, typing_speed)

    def generate_and_plot(self, instance):
        self.button.disabled = True
        self.button.text = "Processing..."
        
        Clock.schedule_once(lambda _: self.process_and_plot())

    def process_and_plot(self):
        seed = self.seed_input.text.strip()
        seed = random.randint(1, 99999999) if seed == '' else int(seed)

        projection_mapping = {
            'Rectilinear': Projection.RECTILINEAR,
            'Polar': Projection.POLAR,
            'Aitoff': Projection.AITOFF,
            'Hammer': Projection.HAMMER,
            'Lambert': Projection.LAMBERT,
            'Mollweide': Projection.MOLLWEIDE
        }
        projection = projection_mapping.get(self.projection_spinner.text, Projection.RECTILINEAR)

        print("\033[1;32mUsing seed =", seed, "\033[0m")
        print("\033[1;32mUsing projection =", projection, "\033[0m")

        output_folder = "Output"
        os.makedirs(output_folder, exist_ok=True)

        filename = str(uuid.uuid4())
        folder_name = os.path.join("Output", filename)
        os.makedirs(folder_name, exist_ok=True)

        config_file_path = os.path.join(folder_name, f"{filename}_config.txt")
        with open(config_file_path, "w") as config_file:
            config_file.write(f"Seed: {seed}\n")
            config_file.write(f"Projection: {self.projection_spinner.text}\n")

        gradient = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r',
                    'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys',
                    'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r',
                    'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r',
                    'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy',
                    'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1',
                    'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r']

        def f1(x, y):
            result = random.uniform(-1,1) * x**3  - math.sin(y**2) + abs(y-x)
            return result
        def f2(x, y):
            result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 9*x
            return result
        def f3(x, y):
            result = random.uniform(-1,1) * x**3  - math.sin(y**2) + abs(y-x)
            return result
        def f4(x, y):
            result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 9*x
            return result

        g1 = GenerativeImage(f1, f2)
        g2 = GenerativeImage(f3, f4)
        g1.generate(seed=seed)
        g2.generate(seed=seed)
        g1.plot(bgcolor="black", projection=projection)
        fig1 = g1.fig
        ax = fig1.get_axes()[0]
        ax.scatter(
            g1.data2,
            g1.data1,
            alpha=0.06,
            cmap=random.choice(gradient),
            c=g1.data2,
            s=0.06,
        )
        ax.scatter(
            g2.data2,
            g2.data1,
            alpha=0.06,
            cmap=random.choice(gradient),
            c=g2.data2,
            s=0.06
        )

        g1.save_image(file_adr=os.path.join(folder_name, f"{filename}.png"), depth=2)
        
        Clock.schedule_once(lambda _: self.update_image_widget(f"{filename}.png"))

    def update_image_widget(self, image_path):
        folder_name = "Output"
        image_folder = os.path.splitext(image_path)[0]
        image_folder = os.path.join(folder_name, image_folder)
        image_path = os.path.join(image_folder, image_path)
        image_path = image_path.replace("\\", "/")
        image_path = os.path.abspath(image_path)
        self.image_widget.source = image_path
        Clock.schedule_once(lambda _: self.enable_button(), 1)

    def enable_button(self):
        self.button.disabled = False
        self.button.text = "Generate and Plot"

if __name__ == '__main__':
    MyApp().run()

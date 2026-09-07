from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
import swisseph as swe
from datetime import datetime

class AstroApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        self.root.add_widget(Label(text="[b]Real Astro Transit Engine[/b]", markup=True, font_size='20sp', size_hint_y=None, height=40))
        
        # Ayanamsha Selector (Manual KP / Lahiri Option)
        ayanamsha_layout = BoxLayout(size_hint_y=None, height=40)
        ayanamsha_layout.add_widget(Label(text="Ayanamsha:"))
        self.ayan_spinner = Spinner(text='KP', values=('KP', 'LAHIRI'))
        ayanamsha_layout.add_widget(self.ayan_spinner)
        self.root.add_widget(ayanamsha_layout)
        
        # Location Defaults (Mumbai, India)
        loc_layout = BoxLayout(size_hint_y=None, height=40)
        self.lat_input = TextInput(text='19.0760', hint_text='Latitude')
        self.lon_input = TextInput(text='72.8777', hint_text='Longitude')
        loc_layout.add_widget(Label(text="Mumbai Coordinates:"))
        loc_layout.add_widget(self.lat_input)
        loc_layout.add_widget(self.lon_input)
        self.root.add_widget(loc_layout)
        
        # Custom Orb Selector
        orb_layout = BoxLayout(size_hint_y=None, height=40)
        orb_layout.add_widget(Label(text="Orb (Degrees):"))
        self.orb_input = TextInput(text='1.0', hint_text='Orb')
        orb_layout.add_widget(self.orb_input)
        self.root.add_widget(orb_layout)
        
        # Action Button
        btn = Button(text="Calculate Transit Data", size_hint_y=None, height=50)
        btn.bind(on_press=self.calculate_transit)
        self.root.add_widget(btn)
        
        # Result Display Area
        self.result_label = Label(text="Click button to load real Swiss Ephemeris data...", size_hint_y=None)
        self.result_label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        scroll = ScrollView()
        scroll.add_widget(self.result_label)
        self.root.add_widget(scroll)
        
        return self.root

    def calculate_transit(self, instance):
        # Ayanamsha Setting
        mode = self.ayan_spinner.text
        swe.set_sid_mode(swe.SIDM_KRISHNAMURTI if mode == 'KP' else swe.SIDM_LAHIRI)
        
        # Current UTC Julian Day Calculation
        now = datetime.utcnow()
        jd = swe.julday(now.year, now.month, now.day, now.hour + now.minute/60.0)
        flags = swe.FLG_SPEED | swe.FLG_SIDEREAL
        
        # Mars Position
        mars_pos, _ = swe.calc_ut(jd, swe.MARS, flags)
        # Mercury Position
        merc_pos, _ = swe.calc_ut(jd, swe.MERCURY, flags)
        
        diff = abs(mars_pos[0] - merc_pos[0]) % 360
        if diff > 180: diff = 360 - diff
        
        orb = float(self.orb_input.text)
        is_conjunction = "YES (In Conjunction)" if diff <= orb else "NO"
        
        res_text = (
            f"Ayanamsha: {mode}\n"
            f"Location: Lat {self.lat_input.text}, Lon {self.lon_input.text}\n"
            f"Mars Longitude: {mars_pos[0]:.2f}°\n"
            f"Mercury Longitude: {merc_pos[0]:.2f}°\n"
            f"Angular Difference: {diff:.2f}°\n"
            f"Conjunction Status (Orb {orb}°): {is_conjunction}\n"
        )
        self.result_label.text = res_text

if __name__ == '__main__':
    AstroApp().run()

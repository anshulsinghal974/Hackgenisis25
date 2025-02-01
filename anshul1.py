from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.spinner import Spinner
from kivymd.uix.pickers import MDTimePicker
from plyer import gps
from kivy.utils import platform

class LocationTimeApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        self.add_widget(Label(text='Choose Location Entry Method:', size_hint=(1, 0.1)))
        
        self.manual_toggle = ToggleButton(text='Manual Entry', group='location', size_hint=(1, 0.1))
        self.manual_toggle.bind(on_press=self.toggle_manual_entry)
        self.add_widget(self.manual_toggle)
        
        self.gps_toggle = ToggleButton(text='Use GPS', group='location', state='down', size_hint=(1, 0.1))
        self.gps_toggle.bind(on_press=self.toggle_manual_entry)
        self.add_widget(self.gps_toggle)
        
        self.location_input = TextInput(hint_text='Enter Address Manually', size_hint=(1, 0.1), disabled=True)
        self.add_widget(self.location_input)
        
        self.gps_button = Button(text='Get GPS Location', size_hint=(1, 0.1))
        self.gps_button.bind(on_press=self.get_gps_location)
        self.add_widget(self.gps_button)
        
        self.add_widget(Label(text='Choose Time Entry Method:', size_hint=(1, 0.1)))
        
        self.time_spinner = Spinner(
            text='Select Time Duration',
            values=('15 mins', '30 mins', '1 hour', '2 hours', 'Custom'),
            size_hint=(1, 0.1)
        )
        self.time_spinner.bind(text=self.on_time_select)
        self.add_widget(self.time_spinner)
        
        self.time_button = Button(text='Pick Time', size_hint=(1, 0.1))
        self.time_button.bind(on_press=self.show_time_picker)
        self.add_widget(self.time_button)
        
        self.custom_time_input = TextInput(hint_text='Enter Custom Time (hh:mm:ss)', size_hint=(1, 0.1), disabled=True)
        self.add_widget(self.custom_time_input)
    
    def toggle_manual_entry(self, instance):
        if self.manual_toggle.state == 'down':
            self.location_input.disabled = False
            self.gps_button.disabled = True
        else:
            self.location_input.disabled = True
            self.gps_button.disabled = False
    
    def get_gps_location(self, instance):
        if platform in ['android', 'ios']:
            try:
                gps.configure(on_location=self.on_gps_location, on_status=self.on_gps_status)
                gps.start()
            except NotImplementedError:
                self.show_popup('GPS Error', 'GPS not supported on this device')
        else:
            self.show_popup('GPS Error', 'GPS feature is not supported on this system')
    
    def on_gps_location(self, **kwargs):
        self.location_input.text = f"Lat: {kwargs['lat']}, Lon: {kwargs['lon']}"
        gps.stop()
    
    def on_gps_status(self, status):
        if status != 'provider-enabled':
            self.show_popup('GPS Error', 'GPS provider is not enabled')
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.6, 0.4))
        popup.open()
    
    def on_time_select(self, spinner, text):
        if text == 'Custom':
            self.custom_time_input.disabled = False
            self.time_button.disabled = False
        else:
            self.custom_time_input.disabled = True
            self.custom_time_input.text = ''
            self.time_button.disabled = True
    
    def show_time_picker(self, instance):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.set_time)
        time_dialog.open()
    
    def set_time(self, instance, time):
        self.custom_time_input.text = str(time)

class MyApp(MDApp):
    def build(self):
        return LocationTimeApp()

if __name__ == '__main__':
    MyApp().run()

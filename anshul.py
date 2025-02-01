from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Ellipse
from kivy.clock import Clock as KivyClock
from kivy.properties import NumericProperty
from plyer import gps
import datetime
import math

class ClockWidget(Widget):
    hour_angle = NumericProperty(0)
    minute_angle = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_hour = 0
        self.selected_minute = 0
        self.bind(pos=self.update_clock, size=self.update_clock)
        
    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            # Clock face
            Color(0.8, 0.8, 0.8, 1)
            center_x = self.center_x
            center_y = self.center_y
            radius = min(self.width, self.height) / 2 * 0.9
            
            # Draw clock circle
            Color(0.9, 0.9, 0.9, 1)
            Ellipse(pos=(center_x - radius, center_y - radius),
                   size=(radius * 2, radius * 2))
            
            # Draw hour markers
            Color(0.2, 0.2, 0.2, 1)
            for i in range(12):
                angle = i * 30  # 360 / 12 = 30 degrees
                rad_angle = math.radians(angle)
                start_pos = (center_x + (radius * 0.8) * math.sin(rad_angle),
                           center_y + (radius * 0.8) * math.cos(rad_angle))
                end_pos = (center_x + radius * math.sin(rad_angle),
                          center_y + radius * math.cos(rad_angle))
                Line(points=[start_pos[0], start_pos[1], end_pos[0], end_pos[1]], width=2)
                
            # Hour numbers
            for i in range(12):
                angle = i * 30
                rad_angle = math.radians(angle)
                number_radius = radius * 0.7
                number_pos = (center_x + number_radius * math.sin(rad_angle),
                            center_y + number_radius * math.cos(rad_angle))
                number = str(12 if i == 0 else i)
                Label(text=number,
                      pos=(number_pos[0] - 10, number_pos[1] - 10),
                      size=(20, 20))
            
            # Hour hand
            Color(0.2, 0, 0, 1)  # Red color
            hour_length = radius * 0.5
            hour_x = center_x + hour_length * math.sin(math.radians(self.hour_angle))
            hour_y = center_y + hour_length * math.cos(math.radians(self.hour_angle))
            Line(points=[center_x, center_y, hour_x, hour_y], width=3)
            
            # Minute hand
            Color(0, 0, 0.8, 1)  # Blue color
            minute_length = radius * 0.7
            minute_x = center_x + minute_length * math.sin(math.radians(self.minute_angle))
            minute_y = center_y + minute_length * math.cos(math.radians(self.minute_angle))
            Line(points=[center_x, center_y, minute_x, minute_y], width=2)
    
    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False
            
        center_x = self.center_x
        center_y = self.center_y
        
        # Calculate angle from touch
        dx = touch.x - center_x
        dy = touch.y - center_y
        angle = math.degrees(math.atan2(dx, dy))
        if angle < 0:
            angle += 360
            
        # Determine if user is setting hours or minutes based on distance from center
        radius = math.sqrt(dx**2 + dy**2)
        max_radius = min(self.width, self.height) / 2
        
        if radius < max_radius * 0.5:  # Inner circle for hours
            self.selected_hour = int(((angle + 15) % 360) / 30)
            if self.selected_hour == 0:
                self.selected_hour = 12
            self.hour_angle = angle
        else:  # Outer circle for minutes
            self.selected_minute = int(((angle + 6) % 360) / 6)
            self.minute_angle = angle
            
        self.update_clock()
        return True

class DonatorPortalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Donation Type
        layout.add_widget(Label(text="Type of Donation:"))
        self.donation_type_input = TextInput(hint_text="Enter donation type")
        layout.add_widget(self.donation_type_input)

        # Preferred Time with Clock
        layout.add_widget(Label(text="Preferred Time:"))
        self.time_button = Button(text="Select Time")
        self.time_button.bind(on_press=self.open_time_picker)
        layout.add_widget(self.time_button)

        # Address Option
        layout.add_widget(Label(text="Address:"))
        self.address_option_layout = BoxLayout(size_hint_y=None, height=40)
        self.manual_button = ToggleButton(text="Enter Manually", group="address", state="down")
        self.gps_button = ToggleButton(text="Use GPS", group="address")
        self.manual_button.bind(on_press=self.toggle_address_input)
        self.gps_button.bind(on_press=self.toggle_address_input)
        self.address_option_layout.add_widget(self.manual_button)
        self.address_option_layout.add_widget(self.gps_button)
        layout.add_widget(self.address_option_layout)

        self.address_input = TextInput(hint_text="Enter your address")
        layout.add_widget(self.address_input)

        # Submit Button
        submit_button = Button(text="Submit Donation")
        submit_button.bind(on_press=self.submit_donation)
        layout.add_widget(submit_button)

        self.add_widget(layout)

    def open_time_picker(self, instance):
        # Create layout for the clock popup
        clock_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Add the clock widget
        self.clock_widget = ClockWidget(size_hint=(1, 0.8))
        clock_layout.add_widget(self.clock_widget)
        
        # Add time display label
        self.time_label = Label(text="12:00", size_hint=(1, 0.1))
        clock_layout.add_widget(self.time_label)
        
        # Add confirm button
        confirm_button = Button(text="Confirm Time", size_hint=(1, 0.1))
        confirm_button.bind(on_press=self.save_time)
        clock_layout.add_widget(confirm_button)
        
        self.popup = Popup(title="Select Time",
                          content=clock_layout,
                          size_hint=(0.9, 0.9))
        self.popup.open()
        
        # Update time label every second
        Clock = KivyClock.schedule_interval(self.update_time_label, 0.1)

    def update_time_label(self, dt):
        if hasattr(self, 'clock_widget'):
            hour = self.clock_widget.selected_hour
            minute = self.clock_widget.selected_minute
            self.time_label.text = f"{hour:02d}:{minute:02d}"

    def save_time(self, instance):
        if hasattr(self, 'clock_widget'):
            hour = self.clock_widget.selected_hour
            minute = self.clock_widget.selected_minute
            self.time_button.text = f"{hour:02d}:{minute:02d}"
        self.popup.dismiss()

    def toggle_address_input(self, instance):
        if self.manual_button.state == "down":
            self.address_input.disabled = False
            self.address_input.text = ""
        else:
            self.address_input.disabled = True
            self.get_gps_location()

    def get_gps_location(self):
        try:
            gps.configure(on_location=self.on_gps_location)
            gps.start()
        except NotImplementedError:
            self.address_input.text = "GPS not available on this device"

    def on_gps_location(self, **kwargs):
        gps.stop()
        location = f"Lat: {kwargs.get('lat')}, Lon: {kwargs.get('lon')}"
        self.address_input.text = location

    def submit_donation(self, instance):
        donation_type = self.donation_type_input.text
        preferred_time = self.time_button.text
        address = self.address_input.text

        confirmation = f"Donation Type: {donation_type}\nPreferred Time: {preferred_time}\nAddress: {address}"
        popup = Popup(title="Donation Submitted", content=Label(text=confirmation), size_hint=(0.8, 0.5))
        popup.open()

class HOPEBRIDGE(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DonatorPortalScreen(name='donator_portal'))
        return sm

if __name__ == "__main__":
    HOPEBRIDGE().run()
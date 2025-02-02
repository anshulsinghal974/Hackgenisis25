from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import ScreenManager
from datetime import datetime, timedelta

# Dictionary of Ahmedabad areas with their coordinates, sample drives, and NGO contact info
AHMEDABAD_AREAS = {
    'navrangpura': {
        'lat': 23.0333,
        'lon': 72.5667,
        'drives': [
            {'time': '10:00 AM', 'date': '2025-02-02'},
            {'time': '2:00 PM', 'date': '2025-02-02'},
            {'time': '11:00 AM', 'date': '2025-02-03'}
        ],
        'ngo_contact': 'NGO: Helping Hands, Contact: +91 123 456 7890'
    },
    'satellite': {
        'lat': 23.0145,
        'lon': 72.5289,
        'drives': [
            {'time': '9:00 AM', 'date': '2025-02-02'},
            {'time': '3:00 PM', 'date': '2025-02-02'},
            {'time': '10:00 AM', 'date': '2025-02-03'}
        ],
        'ngo_contact': 'NGO: Satellite Care, Contact: +91 987 654 3210'
    },
    'vastrapur': {
        'lat': 23.0389,
        'lon': 72.5344,
        'drives': [
            {'time': '11:00 AM', 'date': '2025-02-02'},
            {'time': '4:00 PM', 'date': '2025-02-02'},
            {'time': '9:00 AM', 'date': '2025-02-03'}
        ],
        'ngo_contact': 'NGO: Vastrapur Volunteers, Contact: +91 456 789 0123'
    },
    'paldi': {
        'lat': 23.0117,
        'lon': 72.5634,
        'drives': [
            {'time': '10:30 AM', 'date': '2025-02-02'},
            {'time': '2:30 PM', 'date': '2025-02-02'},
            {'time': '11:30 AM', 'date': '2025-02-03'}
        ],
        'ngo_contact': 'NGO: Paldi Hope, Contact: +91 654 321 9870'
    },
    'bodakdev': {
        'lat': 23.0386,
        'lon': 72.5099,
        'drives': [
            {'time': '9:30 AM', 'date': '2025-02-02'},
            {'time': '3:30 PM', 'date': '2025-02-02'},
            {'time': '10:30 AM', 'date': '2025-02-03'}
        ],
        'ngo_contact': 'NGO: Bodakdev Outreach, Contact: +91 321 987 6540'
    }
}

KV = '''
<VolunteerScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: '16dp'
        spacing: '16dp'
        canvas.before:
            Color:
                rgba: 0.13, 0.55, 0.13, 1  # Forest Green Background
            Rectangle:
                size: self.size
                pos: self.pos

        MDLabel:
            text: 'WE ARE HAPPY THAT YOU CHOSE TO HELP'
            halign: 'center'
            font_style: 'H5'
        
        MDLabel:
            text: "Choose the type of donation drive:"
            halign: 'center'
            font_style: 'H6'

        MDRaisedButton:
            text: 'Food'
            size_hint: None, None
            size: "200dp", "60dp"
            pos_hint: {'center_x': 0.5}
            on_release: root.set_goods('Food')
            md_bg_color: 0.1, 0.7, 0.1, 1  # Green button color
            elevation: 10
            shadow_offset: (2, -2)
            ripple_behavior: True
            outline_color: 0, 0, 0, 0.3
            outline_width: 1
        
        MDRaisedButton:
            text: 'Clothes'
            size_hint: None, None
            size: "200dp", "60dp"
            pos_hint: {'center_x': 0.5}
            on_release: root.set_goods('Clothes')
            md_bg_color: 0.1, 0.7, 0.1, 1
            elevation: 10
            shadow_offset: (2, -2)
            ripple_behavior: True
            outline_color: 0, 0, 0, 0.3
            outline_width: 1
        
        MDRaisedButton:
            text: 'Books'
            size_hint: None, None
            size: "200dp", "60dp"
            pos_hint: {'center_x': 0.5}
            on_release: root.set_goods('Books')
            md_bg_color: 0.1, 0.7, 0.1, 1
            elevation: 10
            shadow_offset: (2, -2)
            ripple_behavior: True
            outline_color: 0, 0, 0, 0.3
            outline_width: 1
        
        MDRaisedButton:
            text: 'Toys'
            size_hint: None, None
            size: "200dp", "60dp"
            pos_hint: {'center_x': 0.5}
            on_release: root.set_goods('Toys')
            md_bg_color: 0.1, 0.7, 0.1, 1
            elevation: 10
            shadow_offset: (2, -2)
            ripple_behavior: True
            outline_color: 0, 0, 0, 0.3
            outline_width: 1
        
        MDRaisedButton:
            text: 'Furniture'
            size_hint: None, None
            size: "200dp", "60dp"
            pos_hint: {'center_x': 0.5}
            on_release: root.set_goods('Furniture')
            md_bg_color: 0.1, 0.7, 0.1, 1
            elevation: 10
            shadow_offset: (2, -2)
            ripple_behavior: True
            outline_color: 0, 0, 0, 0.3
            outline_width: 1

        MDLabel:
            id: selected_goods_label
            text: 'Selected Donation Type: Not selected'
            halign: 'center'
        
        MDRaisedButton:
            text: 'Select Time'
            pos_hint: {'center_x': .5}
            on_release: root.show_time_picker()

        MDLabel:
            id: time_label
            text: 'Selected Time: Not set'
            halign: 'center'
        
        MDTextField:
            id: area_input
            hint_text: "Enter area in Ahmedabad"
            helper_text: "Available areas: Navrangpura, Satellite, Vastrapur, Paldi, Bodakdev"
            helper_text_mode: "on_error"
        
        MDRaisedButton:
            text: 'Find Nearby Drives'
            pos_hint: {'center_x': .5}
            on_release: root.show_drives_on_map()

        MDLabel:
            id: area_label
            text: 'Selected Area: Not selected'
            halign: 'center'

<DriveMapScreen>:
    BoxLayout:
        orientation: 'vertical'
        
        MapView:
            id: mapview
            lat: 23.0225
            lon: 72.5714
            zoom: 12
            
        MDLabel:
            id: drives_label
            size_hint_y: 0.2
            text: 'Available drives will be shown here'
            halign: 'center'
            
        MDRaisedButton:
            text: "Back to Form"
            size_hint: None, None
            size: "200dp", "60dp"
            pos_hint: {"center_x": 0.5}
            on_release: root.go_back()

        MDLabel:
            id: ngo_info_label
            size_hint_y: 0.2
            text: 'NGO Contact Information will be shown here'
            halign: 'center'
'''

class VolunteerScreen(MDScreen):
    def _init_(self, callback=None, **kwargs):
        super()._init_(**kwargs)
        self.callback = callback
        self.selected_time = None
        self.selected_goods = None
        self.selected_area = None
    
    def set_goods(self, goods):
        self.selected_goods = goods
        self.ids.selected_goods_label.text = f'Selected Donation Type: {goods}'
    
    def show_time_picker(self):
        time_picker = MDTimePicker()
        time_picker.bind(on_save=self.on_time_save)
        time_picker.open()
    
    def on_time_save(self, instance, time):
        self.selected_time = time
        self.ids.time_label.text = f'Selected Time: {time.strftime("%I:%M %p")}'
    
    def show_drives_on_map(self):
        area = self.ids.area_input.text.lower().strip()
        if area not in AHMEDABAD_AREAS:
            self.ids.area_input.error = True
            return
            
        self.selected_area = area
        self.ids.area_label.text = f'Selected Area: {area.title()}'
        
        # Create the map screen
        map_screen = DriveMapScreen(area_data=AHMEDABAD_AREAS[area], name='drive_map')
        
        # Add it to the screen manager if it's not already in the manager
        if 'drive_map' not in self.manager.screen_names:
            self.manager.add_widget(map_screen)
        
        # Switch to map screen
        self.manager.current = 'drive_map'

class DriveMapScreen(MDScreen):
    def _init_(self, area_data, **kwargs):
        super()._init_(**kwargs)
        self.area_data = area_data
        
        # Add marker for selected area (representing the main location)
        mapview = self.ids.mapview
        area_marker = MapMarker(
            lat=area_data['lat'],
            lon=area_data['lon'],
            source='area_marker.png'  # Marker icon for area
        )
        mapview.add_marker(area_marker)
        mapview.center_on(area_data['lat'], area_data['lon'])  # Center map on area

        # Add markers for each drive in the area
        for drive in area_data['drives']:
            drive_marker = MapMarker(
                lat=area_data['lat'] + 0.001,  # Slightly offset for visibility (optional)
                lon=area_data['lon'] + 0.001,  # Same as above
                source='drive_marker.png',  # You can use a different icon for drives
            )
            mapview.add_marker(drive_marker)
        
        # Update the drives label with times and dates
        drives_text = "Available drives in this area:\n"
        for drive in area_data['drives']:
            drives_text += f"{drive['date']} at {drive['time']}\n"
        self.ids.drives_label.text = drives_text

        # Show NGO contact information
        self.ids.ngo_info_label.text = f"NGO Contact Info: {area_data['ngo_contact']}"

    def go_back(self):
        self.manager.current = 'volunteer_screen'

class VolunteerApp(MDApp):
    def _init_(self, callback=None, **kwargs):
        super()._init_(**kwargs)
        self.callback = callback
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        Builder.load_string(KV)

        # Create a ScreenManager to manage different screens
        screen_manager = ScreenManager()
        
        # Create VolunteerScreen and add it to ScreenManager
        volunteer_screen = VolunteerScreen(callback=self.callback, name='volunteer_screen')
        screen_manager.add_widget(volunteer_screen)
        
        return screen_manager

def donation_vol():
    def handle_volunteer_info(info):
        print("\nVolunteer Registration Confirmed!")
        print(f"Goods: {info['goods']}")
        print(f"Time: {info['time'].strftime('%I:%M %p')}")
        print(f"Area: {info['area']}")
        return info
    
    app = VolunteerApp(callback=handle_volunteer_info)
    app.run()

if __name__ == "_main_":
    result = donation_vol()
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.garden.mapview import MapView, MapMarker

# Restricted database of needs with only allowed items
ALLOWED_ITEMS = ['food', 'books', 'clothes', 'medicine', 'toys', 'furniture']

NEEDS_DATABASE = {
    'food': [('Downtown Food Bank - urgent need', 23.0225, 72.5714),
             ('North Community Kitchen', 23.0300, 72.5800),
             ('South Food Distribution Center', 23.0100, 72.5600)],
    'books': [('Children\'s Library - textbooks needed', 23.0350, 72.5850),
              ('Senior Center - large print books needed', 23.0400, 72.5900),
              ('Community School Library', 23.0250, 72.5750)],
    'clothes': [('Homeless Shelter - winter clothes needed', 23.0150, 72.5650),
                ('Women\'s Shelter - professional attire needed', 23.0200, 72.5700),
                ('Youth Center - school uniforms needed', 23.0180, 72.5680)],
    'toys': [('Children\'s Hospital', 23.0280, 72.5780),
             ('Family Crisis Center', 23.0320, 72.5820),
             ('Community Center', 23.0260, 72.5760)],
    'medicine': [('Senior Home - urgent need', 23.0380, 72.5880),
                 ('Free Clinic', 23.0450, 72.5950),
                 ('Rural Health Center', 23.0500, 72.6000)],
    'furniture': [('Refugee Center', 23.0550, 72.6050),
                  ('Women\'s Shelter', 23.0600, 72.6100),
                  ('Veterans Center', 23.0650, 72.6150)]
}

KV = '''
<DonationScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: '16dp'
        spacing: '16dp'
        
        MDLabel:
            text: 'Donation Registration'
            halign: 'center'
            font_style: 'H5'
        
        MDLabel:
            text: 'Select the item you want to donate:'
            halign: 'center'
            theme_text_color: "Secondary"
        
        BoxLayout:
            orientation: 'vertical'
            spacing: '10dp'
            size_hint_y: None
            height: self.minimum_height
            pos_hint: {'center_x': 0.5}
            
            MDRaisedButton:
                text: 'Food'
                size_hint_x: None
                width: 200
                pos_hint: {'center_x': 0.5}
                on_release: root.set_item('food')
            MDRaisedButton:
                text: 'Books'
                size_hint_x: None
                width: 200
                pos_hint: {'center_x': 0.5}
                on_release: root.set_item('books')
            MDRaisedButton:
                text: 'Clothes'
                size_hint_x: None
                width: 200
                pos_hint: {'center_x': 0.5}
                on_release: root.set_item('clothes')
            MDRaisedButton:
                text: 'Medicine'
                size_hint_x: None
                width: 200
                pos_hint: {'center_x': 0.5}
                on_release: root.set_item('medicine')
            MDRaisedButton:
                text: 'Toys'
                size_hint_x: None
                width: 200
                pos_hint: {'center_x': 0.5}
                on_release: root.set_item('toys')
            MDRaisedButton:
                text: 'Furniture'
                size_hint_x: None
                width: 200
                pos_hint: {'center_x': 0.5}
                on_release: root.set_item('furniture')
        
        MDLabel:
            id: error_label
            text: ''
            halign: 'center'
            theme_text_color: "Error"
        
        MDLabel:
            id: needs_label
            text: 'Areas of Need will appear here'
            halign: 'center'
        
        MapView:
            id: map_view
            lat: 23.0225
            lon: 72.5714
            zoom: 12
            size_hint_y: None
            height: "300dp"
        
        MDRaisedButton:
            text: 'Find Areas of Need'
            pos_hint: {'center_x': .5}
            on_release: root.find_needs()
'''

class DonationScreen(MDScreen):
    def _init_(self, callback=None, **kwargs):
        super()._init_(**kwargs)
        self.callback = callback
        self.selected_item = None
    
    def set_item(self, item):
        self.selected_item = item
        self.ids.error_label.text = ""
    
    def find_needs(self):
        if not self.selected_item:
            self.ids.error_label.text = "Please select an item to donate"
            self.ids.needs_label.text = ""
            return
        
        self.ids.error_label.text = ""  # Clear any error messages
        
        # Get the needs for the specific item
        if self.selected_item in NEEDS_DATABASE:
            self.ids.needs_label.text = f"These areas need {self.selected_item}:"
            self.ids.map_view.clear_widgets()
            
            # Remove previous markers
            for child in list(self.ids.map_view.children):
                if isinstance(child, MapMarker):
                    self.ids.map_view.remove_widget(child)
            
            for location, lat, lon in NEEDS_DATABASE[self.selected_item]:
                marker = MapMarker(lat=lat, lon=lon)
                self.ids.map_view.add_widget(marker)

class DonationApp(MDApp):
    def _init_(self, callback=None, **kwargs):
        super()._init_(**kwargs)
        self.callback = callback
    
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        Builder.load_string(KV)
        return DonationScreen(callback=self.callback)

def SELF_DONATION():
    def handle_donation_info(info):
        print("\nDonation Information Processed!")
        return info
            
    app = DonationApp(callback=handle_donation_info)
    app.run()
        
# Example usage
if _name_ == "_main_":
    SELF_DONATION()
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

KV = '''
<DonationScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: '10dp'
        spacing: '10dp'
        canvas.before:
            Color:
                rgba: 0, 0.5, 0, 1  # Green Background
            Rectangle:
                size: self.size
                pos: self.pos
        
        MDLabel:
            text: 'Donation Portal'
            font_style: 'H4'
            halign: 'center'
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # White text
        
        MDTextField:
            id: search_field
            hint_text: "Search donation needs..."
            mode: "rectangle"
            size_hint_x: 0.9
            pos_hint: {"center_x": 0.5}
            on_text: root.filter_results(self.text)
        
        ScrollView:
            size_hint_y: None
            height: "250dp"
            MDGridLayout:
                id: category_grid
                cols: 3  # Use 3 columns to spread out the cards
                size_hint_y: None
                height: self.minimum_height
                spacing: "10dp"
                row_default_height: "100dp"
                row_force_default: True
                
        MDLabel:
            id: needs_label
            text: '🔍 Select an item to see donation areas'
            halign: 'center'
            theme_text_color: "Secondary"
        
        MapView:
            id: map_view
            lat: 23.0225
            lon: 72.5714
            zoom: 12
            size_hint_y: None
            height: "300dp"
'''

CATEGORIES = {
    'Food': ['food', ""],
    'Books': ['books', ""],
    'Clothes': ['clothes', ""],
    'Medicine': ['medicine', ""],
    'Toys': ['toys', ""],
    'Furniture': ['furniture', ""],
}

NEEDS_DATABASE = {
    'food': [("Downtown Food Bank - Urgent", 23.0225, 72.5714)],
    'books': [("Children's Library - Textbooks Needed", 23.0350, 72.5850)],
    'clothes': [("Homeless Shelter - Winter Clothes Needed", 23.0150, 72.5650)],
    'toys': [("Children’s Hospital", 23.0280, 72.5780)],
    'medicine': [("Senior Home - Urgent Need", 23.0380, 72.5880)],
    'furniture': [("Refugee Center", 23.0550, 72.6050)],
}

class DonationScreen(MDScreen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        self.selected_item = None
        self.populate_categories()
    
    def populate_categories(self):
        """Creates category cards dynamically"""
        grid = self.ids.category_grid
        for name, (key, icon) in CATEGORIES.items():
            card = MDCard(
                size_hint=(None, None),
                size=(160, 100),
                radius=12,
                elevation=8,
                md_bg_color=(0, 0.5, 0, 0.8),  # Green Theme
                on_release=lambda x, key=key: self.set_item(key)
            )
            box = BoxLayout(orientation='vertical', padding=10, spacing=5)
            label = MDLabel(text=f"{icon} {name}", halign='center', theme_text_color="Custom", text_color=(1, 1, 1, 1))
            box.add_widget(label)
            card.add_widget(box)
            grid.add_widget(card)
    
    def set_item(self, item):
        self.selected_item = item
        self.find_needs()
    
    def find_needs(self):
        """Displays relevant donation centers"""
        if not self.selected_item:
            self.ids.needs_label.text = "⚠ Please select an item"
            return
        
        self.ids.needs_label.text = f"📍 These areas need {self.selected_item}:"
        self.ids.map_view.clear_widgets()
        
        for location, lat, lon in NEEDS_DATABASE.get(self.selected_item, []):
            # Add markers to map for each relevant donation area
            marker = MapMarker(lat=lat, lon=lon)
            self.ids.map_view.add_widget(marker)
            
            # Optionally, we can center the map on the first marker
            if self.selected_item == 'food':
                self.ids.map_view.center_on(lat, lon)  # Change this logic based on item for better UX
            else:
                self.ids.map_view.center_on(lat, lon)
    
    def filter_results(self, query):
        """Filters donation categories based on search query"""
        grid = self.ids.category_grid
        grid.clear_widgets()
        
        for name, (key, icon) in CATEGORIES.items():
            if query.lower() in name.lower():
                card = MDCard(
                    size_hint=(None, None),
                    size=(160, 100),
                    radius=12,
                    elevation=8,
                    md_bg_color=(0, 0.5, 0, 0.8),
                    on_release=lambda x, key=key: self.set_item(key)
                )
                box = BoxLayout(orientation='vertical', padding=10, spacing=5)
                label = MDLabel(text=f"{icon} {name}", halign='center', theme_text_color="Custom", text_color=(1, 1, 1, 1))
                box.add_widget(label)
                card.add_widget(box)
                grid.add_widget(card)

class DonationApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        Builder.load_string(KV)
        return DonationScreen()

if _name_ == "_main_":
    DonationApp().run()
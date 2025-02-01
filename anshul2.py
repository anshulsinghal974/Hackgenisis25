from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class VolunteerApp(App):
    def build(self):
        Window.title = "Volunteer"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        title_label = Label(text="Choose a Volunteering Option", font_size=24, size_hint=(1, 0.2))
        layout.add_widget(title_label)
        
        button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.6))
        
        mental_wellbeing_btn = Button(text="Mental Wellbeing", size_hint=(1, 1))
        donate_btn = Button(text="Volunteer to Give Donations", size_hint=(1, 1))
        collect_btn = Button(text="Volunteer to Collect Donations", size_hint=(1, 1))
        
        button_layout.add_widget(mental_wellbeing_btn)
        button_layout.add_widget(donate_btn)
        button_layout.add_widget(collect_btn)
        
        layout.add_widget(button_layout)
        
        return layout

if __name__ == "__main__":
    VolunteerApp().run()

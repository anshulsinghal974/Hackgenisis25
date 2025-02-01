from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class UserApp(App):
    def build(self):
        Window.title = "User"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        title_label = Label(text="Choose a Donation Option", font_size=24, size_hint=(1, 0.2))
        layout.add_widget(title_label)
        
        button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.6))
        
        mental_wellbeing_btn = Button(text="Mental Wellbeing", size_hint=(1, 1))
        self_donation_btn = Button(text="Self Donation", size_hint=(1, 1))
        volunteer_donation_btn = Button(text="Donate Through Volunteers", size_hint=(1, 1))
        
        button_layout.add_widget(mental_wellbeing_btn)
        button_layout.add_widget(self_donation_btn)
        button_layout.add_widget(volunteer_donation_btn)
        
        layout.add_widget(button_layout)
        
        return layout

if __name__ == "__main__":
    UserApp().run()

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.core.window import Window
import random

# Set window size
Window.size = (400, 600)

# Define the KV design language string
kv = '''
#:import random random

<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        
        Label:
            text: 'Wellness Counseling'
            font_size: '24sp'
            size_hint_y: None
            height: '60dp'
        
        Button:
            text: 'Mental Health'
            on_press: root.manager.current = 'mental'
            background_color: 0.2, 0.6, 1, 1
            size_hint_y: None
            height: '60dp'
        
        Button:
            text: 'Nutrition'
            on_press: root.manager.current = 'nutrition'
            background_color: 0.2, 0.8, 0.2, 1
            size_hint_y: None
            height: '60dp'
        
        Button:
            text: 'Exercise'
            on_press: root.manager.current = 'exercise'
            background_color: 0.8, 0.2, 0.2, 1
            size_hint_y: None
            height: '60dp'
            
        Button:
            text: 'Daily Plan'
            on_press: root.manager.current = 'daily'
            background_color: 0.8, 0.6, 0.2, 1
            size_hint_y: None
            height: '60dp'

<ContentScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        
        Label:
            text: root.title
            font_size: '24sp'
            size_hint_y: None
            height: '60dp'
        
        Spinner:
            id: category_spinner
            text: 'Select Category'
            values: root.categories
            size_hint_y: None
            height: '50dp'
        
        Button:
            text: 'Get Tip'
            on_press: root.get_tip()
            size_hint_y: None
            height: '50dp'
            background_color: root.button_color
        
        Label:
            id: tip_label
            text: ''
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]
            padding: 10, 10
        
        Widget:
            size_hint_y: 1
        
        Button:
            text: 'Back to Menu'
            on_press: root.manager.current = 'menu'
            size_hint_y: None
            height: '50dp'
            background_color: 0.5, 0.5, 0.5, 1

<DailyPlanScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        
        Label:
            text: 'Daily Wellness Plan'
            font_size: '24sp'
            size_hint_y: None
            height: '60dp'
        
        ScrollView:
            size_hint_y: 1
            
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: 10
                spacing: 10
                
                Label:
                    id: plan_label
                    text: ''
                    text_size: self.width, None
                    size_hint_y: None
                    height: self.texture_size[1]
        
        Button:
            text: 'Generate New Plan'
            on_press: root.generate_plan()
            size_hint_y: None
            height: '50dp'
            background_color: 0.8, 0.6, 0.2, 1
        
        Button:
            text: 'Back to Menu'
            on_press: root.manager.current = 'menu'
            size_hint_y: None
            height: '50dp'
            background_color: 0.5, 0.5, 0.5, 1
'''

class MenuScreen(Screen):
    pass

class ContentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tips = {}
        self.categories = []
        self.title = ''
        self.button_color = (1, 1, 1, 1)

    def get_tip(self):
        category = self.ids.category_spinner.text
        if category in self.tips:
            tip = random.choice(self.tips[category])
            self.ids.tip_label.text = tip

class DailyPlanScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mental_health_tips = {
            'morning': ["Establish a daily routine", "Practice gratitude journaling"],
            'afternoon': ["Take a mindful walk", "Practice deep breathing"],
            'evening': ["Write in your journal", "Do progressive relaxation"]
        }
        self.nutrition_tips = {
            'morning': ["Start with a balanced breakfast", "Drink water with lemon"],
            'afternoon': ["Eat a protein-rich lunch", "Have a healthy snack"],
            'evening': ["Practice mindful eating", "Prepare tomorrow's meals"]
        }
        self.exercise_tips = {
            'morning': ["Morning stretch routine", "Sun Salutation yoga"],
            'afternoon': ["Take a brisk walk", "Do desk exercises"],
            'evening': ["Light yoga session", "Relaxation stretches"]
        }

    def generate_plan(self):
        plan_text = "[b]Morning:[/b]\n"
        plan_text += f"🧠 Mental Health: {random.choice(self.mental_health_tips['morning'])}\n"
        plan_text += f"🥗 Nutrition: {random.choice(self.nutrition_tips['morning'])}\n"
        plan_text += f"💪 Exercise: {random.choice(self.exercise_tips['morning'])}\n\n"

        plan_text += "[b]Afternoon:[/b]\n"
        plan_text += f"🧠 Mental Health: {random.choice(self.mental_health_tips['afternoon'])}\n"
        plan_text += f"🥗 Nutrition: {random.choice(self.nutrition_tips['afternoon'])}\n"
        plan_text += f"💪 Exercise: {random.choice(self.exercise_tips['afternoon'])}\n\n"

        plan_text += "[b]Evening:[/b]\n"
        plan_text += f"🧠 Mental Health: {random.choice(self.mental_health_tips['evening'])}\n"
        plan_text += f"🥗 Nutrition: {random.choice(self.nutrition_tips['evening'])}\n"
        plan_text += f"💪 Exercise: {random.choice(self.exercise_tips['evening'])}\n"

        self.ids.plan_label.text = plan_text
        self.ids.plan_label.markup = True

class WellnessApp(App):
    def build(self):
        # Load the KV design language string
        Builder.load_string(kv)
        
        # Create the screen manager
        sm = ScreenManager()
        
        # Add menu screen
        sm.add_widget(MenuScreen(name='menu'))
        
        # Add mental health screen
        mental_screen = ContentScreen(name='mental')
        mental_screen.title = 'Mental Health'
        mental_screen.categories = ['stress', 'anxiety', 'mood']
        mental_screen.tips = {
            'stress': [
                "Practice deep breathing exercises - try 4-7-8 breathing",
                "Take a mindful walk in nature",
                "Write your thoughts in a journal",
                "Try progressive muscle relaxation",
                "Take regular breaks from work/screens"
            ],
            'anxiety': [
                "Ground yourself using the 5-4-3-2-1 technique",
                "Challenge negative thought patterns",
                "Practice mindfulness meditation",
                "Maintain a regular sleep schedule",
                "Connect with supportive friends or family"
            ],
            'mood': [
                "Establish a daily routine",
                "Get exposure to natural sunlight",
                "Engage in activities you enjoy",
                "Practice gratitude journaling",
                "Set small, achievable goals"
            ]
        }
        mental_screen.button_color = (0.2, 0.6, 1, 1)
        sm.add_widget(mental_screen)
        
        # Add nutrition screen
        nutrition_screen = ContentScreen(name='nutrition')
        nutrition_screen.title = 'Nutrition'
        nutrition_screen.categories = ['general', 'energy', 'mindful eating']
        nutrition_screen.tips = {
            'general': [
                "Eat a rainbow of fruits and vegetables daily",
                "Stay hydrated - aim for 8 glasses of water",
                "Include protein in every meal",
                "Choose whole grains over refined grains",
                "Limit processed foods and added sugars"
            ],
            'energy': [
                "Start your day with a balanced breakfast",
                "Eat small meals every 3-4 hours",
                "Include healthy fats like nuts and avocados",
                "Choose complex carbohydrates for sustained energy",
                "Consider timing meals around your activities"
            ],
            'mindful eating': [
                "Eat slowly and without distractions",
                "Listen to your body's hunger and fullness cues",
                "Use smaller plates to control portions",
                "Practice mindful eating meditation",
                "Plan meals in advance"
            ]
        }
        nutrition_screen.button_color = (0.2, 0.8, 0.2, 1)
        sm.add_widget(nutrition_screen)
        
        # Add exercise screen
        exercise_screen = ContentScreen(name='exercise')
        exercise_screen.title = 'Exercise'
        exercise_screen.categories = ['yoga', 'cardio', 'strength']
        exercise_screen.tips = {
            'yoga': [
                "Sun Salutation sequence for morning energy",
                "Child's Pose for stress relief",
                "Cat-Cow stretches for spine health",
                "Warrior poses for strength and balance",
                "Corpse Pose for relaxation"
            ],
            'cardio': [
                "Take a 30-minute brisk walk",
                "Try interval training",
                "Dance to your favorite music",
                "Use stairs instead of elevator",
                "Go for a bike ride"
            ],
            'strength': [
                "Bodyweight squats and lunges",
                "Push-ups (modified if needed)",
                "Plank holds for core strength",
                "Resistance band exercises",
                "Dumbbell exercises for major muscle groups"
            ]
        }
        exercise_screen.button_color = (0.8, 0.2, 0.2, 1)
        sm.add_widget(exercise_screen)
        
        # Add daily plan screen
        sm.add_widget(DailyPlanScreen(name='daily'))
        
        return sm

if __name__ == '__main__':
    WellnessApp().run()
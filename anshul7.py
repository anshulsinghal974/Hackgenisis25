from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.graphics import Color
from kivy.graphics import Rectangle

# Main Menu Screen
class MainMenuScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        layout.add_widget(Label(text="WELCOME TO WELL-BEING", font_size=55, bold=True, italic=True))

        mental_button = Button(text="Mental Well-being", size_hint_y=None, height=50)
        mental_button.bind(on_press=self.go_to_mental)
        consumption_button = Button(text="Consumption", size_hint_y=None, height=50)
        consumption_button.bind(on_press=self.go_to_consumption)
        physical_button = Button(text="Physical Well-being", size_hint_y=None, height=50)
        physical_button.bind(on_press=self.go_to_physical)

        layout.add_widget(mental_button)
        layout.add_widget(consumption_button)
        layout.add_widget(physical_button)

        self.add_widget(layout)

    def go_to_mental(self, instance):
        self.manager.current = 'mental'

    def go_to_consumption(self, instance):
        self.manager.current = 'consumption'

    def go_to_physical(self, instance):
        self.manager.current = 'physical'

# Mental Well-being Screen
class MentalScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(Label(text="Choose Mental well-being Tracker", font_size=50, bold=True, italic=True))


        mood_button = Button(text="Mood Tracker", size_hint_y=None, height=50)
        mood_button.bind(on_press=self.go_to_mood_tracker)
        sleep_button = Button(text="Sleep Tracker", size_hint_y=None, height=50)
        sleep_button.bind(on_press=self.go_to_sleep_tracker)
        stress_button = Button(text="Stress Level Calculator", size_hint_y=None, height=50)
        stress_button.bind(on_press=self.go_to_stress_tracker)
        back_button = Button(text="Back to Main Menu", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)

        layout.add_widget(mood_button)
        layout.add_widget(sleep_button)
        layout.add_widget(stress_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

    def go_to_mood_tracker(self, instance):
        self.manager.current = 'mood_tracker'

    def go_to_sleep_tracker(self, instance):
        self.manager.current = 'sleep_tracker'

    def go_to_stress_tracker(self, instance):
        self.manager.current = 'stress_tracker'

# Mood Tracker Screen
class MoodTrackerScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Create a horizontal BoxLayout for the image and the mood tracker widgets
        mood_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=550)

        # Add the Image widget
        img = Image(source="C:/Users/nuzha/HACKGENESIS_25/emotion.jpg", size_hint=(None, None), size=(550, 550))
        mood_layout.add_widget(img)

        # Create a vertical BoxLayout for the labels, spinner, and text input (beside the image)
        mood_info_layout = BoxLayout(orientation='vertical', size_hint_x=0.8, padding=10, spacing=10)

        # Label to display the mood tracker message
        mood_info_layout.add_widget(Label(text="Select your mood", bold=True, italic=True, font_size=20))

        # Create a Spinner (dropdown) for selecting mood
        self.mood_spinner = Spinner(
            text="SELECT MOOD",
            values=("Happy", "Sad", "Angry", "Excited", "Stressed", "Relaxed", "Bored", "Tired"),
            size_hint_y=None,
            height=50
        )
        self.mood_spinner.bind(text=self.on_mood_select)  # Bind the selected mood to a function
        mood_info_layout.add_widget(self.mood_spinner)

        # Label to display the selected mood
        self.selected_mood_label = Label(text="Selected Mood: None", bold=True,italic=True,font_size=20)
        mood_info_layout.add_widget(self.selected_mood_label)

        # Text input to ask why the mood is that way
        self.mood_reason_input = TextInput(hint_text="Why do you feel this way?", size_hint_y=None, height=100, multiline=True)
        mood_info_layout.add_widget(self.mood_reason_input)

        # Add the vertical mood layout to the horizontal mood layout
        mood_layout.add_widget(mood_info_layout)

        # Add the mood_layout to the main layout
        layout.add_widget(mood_layout)

        # Button to submit mood data
        submit_button = Button(text="Submit Mood Data", size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_mood)

        # Back button to return to the mental well-being screen
        back_button = Button(text="Back to Mental Well-being", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)

        layout.add_widget(submit_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def on_mood_select(self, spinner, text):
        """This function is called when a mood is selected from the spinner."""
        self.selected_mood_label.text = f"Selected Mood: {text}"

    def submit_mood(self, instance):
        """Function to handle the submission of mood data."""
        mood = self.mood_spinner.text
        reason = self.mood_reason_input.text
        print(f"Selected Mood: {mood}, Reason: {reason}")  # Handle data as needed

    def go_back(self, instance):
        self.manager.current = 'mental'

# Sleep Tracker Screen
class SleepTrackerScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Create a BoxLayout for the image and label to appear side by side
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=500)
        
        # Add Image widget
        img = Image(source="C:/Users/nuzha/HACKGENESIS_25/sleep.jpg", size_hint=(None, None), size=(500, 500))
        top_layout.add_widget(img)

        # Add Label beside the image
        label = Label(text="TRACK YOUR SLEEP INTAKE\n"
                            "Sleep is the best Meditation", font_size=25, bold=True, italic=True, size_hint_x=None, width=500)
        top_layout.add_widget(label)

        # Add top_layout to the main layout
        layout.add_widget(top_layout)


        # Hours of sleep
        self.sleep_hours_input = TextInput(hint_text="Hours of Sleep", size_hint_y=None, height=50, multiline=False)
        layout.add_widget(self.sleep_hours_input)

        # Quality of sleep
        self.sleep_quality_input = TextInput(hint_text="Quality of Sleep (1-10)", size_hint_y=None, height=50, multiline=False)
        layout.add_widget(self.sleep_quality_input)

        # Button to submit sleep data
        submit_button = Button(text="Submit Sleep Data", size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_sleep)
        back_button = Button(text="Back to Mental Well-being", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)

        layout.add_widget(submit_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_sleep(self, instance):
        hours = self.sleep_hours_input.text
        quality = self.sleep_quality_input.text
        print(f"Hours of Sleep: {hours}, Sleep Quality: {quality}")  # Handle data as needed

    def go_back(self, instance):
        self.manager.current = 'mental'

# Stress Level Tracker Screen
class StressTrackerScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        layout.add_widget(Label(text="Rate your stress level from 0 to 10", font_size=18))

        self.stress_slider = Slider(min=0, max=10, value=5)
        self.stress_slider.bind(value=self.on_slider_value_change)
        layout.add_widget(self.stress_slider)

        # Display Stress Level
        self.stress_level_label = Label(text="Stress Level: 5", font_size=18)
        layout.add_widget(self.stress_level_label)

        # Display tips based on stress level
        self.stress_tips_label = Label(text="Tips to manage stress: Take a deep breath.", font_size=18)
        layout.add_widget(self.stress_tips_label)

        submit_button = Button(text="Submit Stress Level", size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_stress)
        back_button = Button(text="Back to Mental Well-being", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)

        layout.add_widget(submit_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def on_slider_value_change(self, instance, value):
        # Update the stress level display
        self.stress_level_label.text = f"Stress Level: {int(value)}"
        
        # Provide tips based on the stress level
        if value <= 3:
            self.stress_tips_label.text = "Tips to maintain low stress: Keep doing things that make you happy and relaxed!"
        elif value <= 7:
            self.stress_tips_label.text = "Tips to reduce stress: Take short breaks, practice deep breathing, and stay organized."
        else:
            self.stress_tips_label.text = "Tips to reduce high stress: Try relaxation techniques like yoga, deep breathing, or talking to someone."

    def submit_stress(self, instance):
        stress_level = self.stress_slider.value
        print(f"Stress level recorded: {stress_level}")  # Handle the data as you need

    def go_back(self, instance):
        self.manager.current = 'mental'

#consumption screen
class ConsumptionScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Label to display the consumption tracker message
        layout.add_widget(Label(text="Choose Consumption Tracker", font_size=50, bold=True, italic=True))

        # Button for Water Intake Tracker
        water_button = Button(text="Water Intake Tracker", size_hint_y=None, height=50)
        water_button.bind(on_press=self.go_to_water_tracker)
        layout.add_widget(water_button)

        # Button for Nutrition Intake Tracker
        nutrition_button = Button(text="Nutrition Intake Tracker", size_hint_y=None, height=50)
        nutrition_button.bind(on_press=self.go_to_nutrition_tracker)
        layout.add_widget(nutrition_button)

        # Back button to return to the main menu
        back_button = Button(text="Back to Main Menu", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_water_tracker(self, instance):
        self.manager.current = 'water_tracker'

    def go_to_nutrition_tracker(self, instance):
        self.manager.current = 'nutrition_tracker'

    def go_back(self, instance):
        self.manager.current = 'main'

#water tracker
class WaterTrackerScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Create a BoxLayout for the image and label to appear side by side
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=500)
        
        # Add Image widget
        img = Image(source="C:/Users/nuzha/HACKGENESIS_25/water.jpg", size_hint=(None, None), size=(500, 500))
        top_layout.add_widget(img)

        # Add Label beside the image
        label = Label(text="TRACK YOUR WATER INTAKE\n"
                            "           Water is life", font_size=25, bold=True, italic=True, size_hint_x=None, width=500)
        top_layout.add_widget(label)

        # Add top_layout to the main layout
        layout.add_widget(top_layout)
  

        # Input field for the user to track their daily water intake
        self.water_input = TextInput(hint_text="Enter water intake in liters", size_hint_y=None, height=50)
        layout.add_widget(self.water_input)

        # Button to submit the water intake data
        submit_button = Button(text="Submit Water Intake", size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_water_intake)
        layout.add_widget(submit_button)

        # Back button to go back to the Consumption screen
        back_button = Button(text="Back to Consumption", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_water_intake(self, instance):
        water_intake = self.water_input.text
        print(f"Water Intake Submitted: {water_intake} liters")  # Handle this data as needed

    def go_back(self, instance):
        self.manager.current = 'consumption'

#nutrition tracker
class NutritionTrackerScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Create a BoxLayout for the image and label to appear side by side
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=500)
        
        # Add Image widget
        img = Image(source="C:/Users/nuzha/HACKGENESIS_25/nutrition.jpg", size_hint=(None, None), size=(500, 500))
        top_layout.add_widget(img)

        # Add Label beside the image
        label = Label(text="TRACK YOUR NUTRITION INTAKE\n"
                            "       You Are What You eat", font_size=25, bold=True, italic=True, size_hint_x=None, width=500)
        top_layout.add_widget(label)

        # Add top_layout to the main layout
        layout.add_widget(top_layout)

        # Input field for the user to track their daily nutrition intake
        self.nutrition_input = TextInput(hint_text="Enter your nutrition intake details in calories", size_hint_y=None, height=100, multiline=True)
        layout.add_widget(self.nutrition_input)

        # Button to submit the nutrition intake data
        submit_button = Button(text="Submit Nutrition Intake", size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_nutrition_intake)
        layout.add_widget(submit_button)

        # Back button to go back to the Consumption screen
        back_button = Button(text="Back to Consumption", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_nutrition_intake(self, instance):
        nutrition_intake = self.nutrition_input.text
        print(f"Nutrition Intake Submitted: {nutrition_intake}")  # Handle this data as needed

    def go_back(self, instance):
        self.manager.current = 'consumption'


class PhysicalScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        layout.add_widget(Label(text="Choose physical-wellbeing tracker", font_size=50, bold=True, italic=True))

        # Buttons for Physical Well-being options
        exercise_button = Button(text="Exercise Tracker", size_hint_y=None, height=50)
        exercise_button.bind(on_press=self.go_to_exercise_tracker)
        yoga_button = Button(text="Yoga and Meditation Tracker", size_hint_y=None, height=50)
        yoga_button.bind(on_press=self.go_to_yoga_meditation_tracker)

        back_button = Button(text="Back to Main Menu", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)

        layout.add_widget(exercise_button)
        layout.add_widget(yoga_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_exercise_tracker(self, instance):
        self.manager.current = 'exercise_tracker'

    def go_to_yoga_meditation_tracker(self, instance):
        self.manager.current = 'yoga_meditation_tracker'

    def go_back(self, instance):
        self.manager.current = 'main'

class ExerciseTrackerScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)

        with self.canvas.before:
            Color(0.533, 0.733, 0.333, 1)  # pistachio 
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Update the rectangle when the window size changes
        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=500)


        # Add Image widget
        img = Image(source="C:/Users/nuzha/HACKGENESIS_25/gym.jpg", size_hint=(None, None), size=(500, 500))
        top_layout.add_widget(img)

        # Add Label beside the image
        label = Label(text="TRACK YOUR EXERCISES\n"
                            "               Work It", font_size=25, bold=True, italic=True, size_hint_x=None, width=500)
        top_layout.add_widget(label)

        # Add top_layout to the main layout
        layout.add_widget(top_layout)


        # Input field to track time spent on exercise
        self.exercise_input = TextInput(hint_text="Enter exercise time in minutes",size_hint_y=None,height=50)
        layout.add_widget(self.exercise_input)

        # Button to submit exercise data
        submit_button = Button(text="Submit Exercise Data", size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_exercise)
        layout.add_widget(submit_button)

        # Back button to go back to the Physical Well-being screen
        back_button = Button(text="Back to Physical Well-being", size_hint_y=None, height=50,
                             background_normal='', background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_exercise(self, instance):
        exercise_time = self.exercise_input.text
        print(f"Exercise Time Submitted: {exercise_time} minutes")  # Handle this data as needed

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_back(self, instance):
        self.manager.current = 'physical'


class YogaMeditationTrackerScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)

        # Add background color
        with self.canvas.before:
            Color(0.533, 0.733, 0.333, 1)  # pistachio 
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Update the rectangle when the window size changes
        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Create a BoxLayout for the image and label to appear side by side
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=500)

        # Add Image widget
        img = Image(source="C:/Users/nuzha/HACKGENESIS_25/meditation.jpg", size_hint=(None, None), size=(500, 500))
        top_layout.add_widget(img)

        # Add Label beside the image
        label = Label(text="TRACK YOUR MEDITATION\n~Breathe In And Breathe Out~", 
                      font_size=25, bold=True, italic=True, size_hint_x=None, width=500, color=(0.172, 0.373, 0.176, 1))
        top_layout.add_widget(label)

        # Add top_layout to the main layout
        layout.add_widget(top_layout)

        # Input field to track time spent on yoga or meditation
        self.yoga_meditation_input = TextInput(hint_text="Enter time spent on meditation in minutes", size_hint_y=None, height=50,
                                               background_normal='', background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        layout.add_widget(self.yoga_meditation_input)

        # Button to submit yoga/meditation data
        submit_button = Button(text="Submit Yoga/Meditation Data", size_hint_y=None, 
                               height=50, background_normal='', background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        submit_button.bind(on_press=self.submit_yoga_meditation)
        layout.add_widget(submit_button)

        # Back button to go back to the Physical Well-being screen
        back_button = Button(text="Back to Physical Well-being", size_hint_y=None, height=50,background_normal='', 
                             background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def submit_yoga_meditation(self, instance):
        yoga_meditation_time = self.yoga_meditation_input.text
        print(f"Yoga/Meditation Time Submitted: {yoga_meditation_time} minutes")

    def go_back(self, instance):
        self.manager.current = 'physical'



class HOPEBRIDGE(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PhysicalScreen(name='physical'))  
        sm.add_widget(MainMenuScreen(name='main'))
        sm.add_widget(MentalScreen(name='mental'))
        sm.add_widget(MoodTrackerScreen(name='mood_tracker'))
        sm.add_widget(StressTrackerScreen(name='stress_tracker'))
        sm.add_widget(SleepTrackerScreen(name='sleep_tracker'))
        sm.add_widget(ConsumptionScreen(name='consumption'))
        sm.add_widget(WaterTrackerScreen(name='water_tracker'))
        sm.add_widget(NutritionTrackerScreen(name='nutrition_tracker'))
        sm.add_widget(ExerciseTrackerScreen(name='exercise_tracker'))
        sm.add_widget(YogaMeditationTrackerScreen(name='yoga_meditation_tracker'))
        return sm

    
if _name_ == "_main_":
    HOPEBRIDGE().run()
import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.utils import get_color_from_hex
from kivy.metrics import dp

#consumption screen
class ConsumptionScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        with self.canvas.before:
            Color(0.533, 0.733, 0.333, 1)  # pistachio 
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Update the rectangle when the window size changes
        self.bind(size=self._update_rect, pos=self._update_rect)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Label to display the consumption tracker message
        layout.add_widget(Label(text="Choose Consumption Tracker", font_size=50, bold=True, italic=True,color=(0.172, 0.373, 0.176, 1)))

        # Button for Water Intake Tracker
        water_button = Button(text="Water Intake Tracker", size_hint_y=None, height=50,background_normal='', 
                              background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        water_button.bind(on_press=self.go_to_water_tracker)
        layout.add_widget(water_button)

        # Button for Nutrition Intake Tracker
        nutrition_button = Button(text="Nutrition Intake Tracker", size_hint_y=None, height=50,background_normal='', 
                                  background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        nutrition_button.bind(on_press=self.go_to_nutrition_tracker)
        layout.add_widget(nutrition_button)

        # Back button to return to the main menu
        back_button = Button(text="Back to Main Menu", size_hint_y=None, height=50,background_normal='',
                              background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)
    
    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

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
        img = Image(source="C:/Users/nuzha/HACKGENESIS_25/water.jpg", size_hint=(None, None), size=(500, 500))
        top_layout.add_widget(img)

        # Add Label beside the image
        label = Label(text="TRACK YOUR WATER INTAKE\n"
                            "           Water is life", font_size=25, bold=True, italic=True, size_hint_x=None, width=500,
                                                            color=(0.172, 0.373, 0.176, 1))
        top_layout.add_widget(label)

        # Add top_layout to the main layout
        layout.add_widget(top_layout)
  

        # Input field for the user to track their daily water intake
        self.water_input = TextInput(hint_text="Enter water intake in liters", size_hint_y=None, height=50,background_normal='',
                                      background_color = (1, 1, 0.733, 1))
        layout.add_widget(self.water_input)

        # Button to submit the water intake data
        submit_button = Button(text="Submit Water Intake", size_hint_y=None, height=50,
                               background_normal='', background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        submit_button.bind(on_press=self.submit_water_intake)
        layout.add_widget(submit_button)

        # Back button to go back to the Consumption screen
        back_button = Button(text="Back to Consumption", size_hint_y=None, height=50,background_normal='',
                              background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_water_intake(self, instance):
        water_intake = self.water_input.text
        print(f"Water Intake Submitted: {water_intake} liters")  # Handle this data as needed

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_back(self, instance):
        self.manager.current = 'consumption'

#nutrition tracker
class NutritionTrackerScreen(Screen):
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
        img = Image(source="C:/Users/nuzha/HACKGENESIS_25/nutrition.jpg", size_hint=(None, None), size=(500, 500))
        top_layout.add_widget(img)

        # Add Label beside the image
        label = Label(text="TRACK YOUR NUTRITION INTAKE\n"
                            "       You Are What You eat", font_size=25, bold=True, italic=True, size_hint_x=None, width=500,
                                                            color=(0.172, 0.373, 0.176, 1))
        top_layout.add_widget(label)

        # Add top_layout to the main layout
        layout.add_widget(top_layout)

        # Input field for the user to track their daily nutrition intake
        self.nutrition_input = TextInput(hint_text="Enter your nutrition intake details in calories", size_hint_y=None, height=100,
                                         background_normal='', background_color = (1, 1, 0.733, 1), multiline=True)
        layout.add_widget(self.nutrition_input)

        # Button to submit the nutrition intake data
        submit_button = Button(text="Submit Nutrition Intake", size_hint_y=None, height=50,background_normal='', 
                               background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        submit_button.bind(on_press=self.submit_nutrition_intake)
        layout.add_widget(submit_button)

        # Back button to go back to the Consumption screen
        back_button = Button(text="Back to Consumption", size_hint_y=None, height=50,background_normal='', 
                             background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def submit_nutrition_intake(self, instance):
        nutrition_intake = self.nutrition_input.text
        print(f"Nutrition Intake Submitted: {nutrition_intake}")  # Handle this data as needed

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_back(self, instance):
        self.manager.current = 'consumption'


class PhysicalScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)
        with self.canvas.before:
            Color(0.533, 0.733, 0.333, 1)  # pistachio 
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Update the rectangle when the window size changes
        self.bind(size=self._update_rect, pos=self._update_rect)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        layout.add_widget(Label(text="Choose physical-wellbeing tracker", font_size=50, bold=True, italic=True,color=(0.172, 0.373, 0.176, 1)))

        # Buttons for Physical Well-being options
        exercise_button = Button(text="Exercise Tracker", size_hint_y=None, height=50,background_normal='', background_color = (1, 1, 0.733, 1),
                                 color=(0.172, 0.373, 0.176, 1))
        exercise_button.bind(on_press=self.go_to_exercise_tracker)

        yoga_button = Button(text="Yoga and Meditation Tracker", size_hint_y=None, height=50,
                             background_normal='', background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        yoga_button.bind(on_press=self.go_to_yoga_meditation_tracker)

        back_button = Button(text="Back to Main Menu", size_hint_y=None, height=50,background_normal='', 
                             background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        back_button.bind(on_press=self.go_back)

        layout.add_widget(exercise_button)
        layout.add_widget(yoga_button)
        layout.add_widget(back_button)

        self.add_widget(layout)
    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_to_exercise_tracker(self, instance):
        self.manager.current = 'exercise_tracker'

    def go_to_yoga_meditation_tracker(self, instance):
        self.manager.current = 'yoga_meditation_tracker'

    def go_back(self, instance):
        self.manager.current = 'main'

class ExerciseTrackerScreen(Screen):
    def _init_(self, **kwargs):
        super()._init_(**kwargs)

        # Add background color
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
                            "               Work It", font_size=25, bold=True, italic=True, size_hint_x=None, width=500,
                                                        color=(0.172, 0.373, 0.176, 1))
        top_layout.add_widget(label)

        # Add top_layout to the main layout
        layout.add_widget(top_layout)


        # Input field to track time spent on exercise
        self.exercise_input = TextInput(hint_text="Enter exercise time in minutes",size_hint_y=None,height=50,background_normal='',
                                         background_color = (1, 1, 0.733, 1))
        layout.add_widget(self.exercise_input)

        # Button to submit exercise data
        submit_button = Button(text="Submit Exercise Data", size_hint_y=None, height=50,background_normal='',
                                background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        submit_button.bind(on_press=self.submit_exercise)
        layout.add_widget(submit_button)

        # Back button to go back to the Physical Well-being screen
        back_button = Button(text="Back to Physical Well-being", size_hint_y=None, height=50,background_normal='', 
                             background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
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
        label = Label(text="TRACK YOUR MEDITATION\n"
                      "Breathe In And Breathe Out", 
                      font_size=25, bold=True, italic=True, size_hint_x=None, width=500, color=(0.172, 0.373, 0.176, 1))
        top_layout.add_widget(label)

        # Add top_layout to the main layout
        layout.add_widget(top_layout)

        # Input field to track time spent on yoga or meditation
        self.yoga_meditation_input = TextInput(hint_text="Enter time spent on meditation in minutes", size_hint_y=None, 
                                               height=50, background_normal='', background_color = (1, 1, 0.733, 1))
        layout.add_widget(self.yoga_meditation_input)

        # Button to submit yoga/meditation data
        submit_button = Button(text="Submit Yoga/Meditation Data", size_hint_y=None, 
                               height=50,background_normal='', background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
        submit_button.bind(on_press=self.submit_yoga_meditation)
        layout.add_widget(submit_button)

        # Back button to go back to the Physical Well-being screen
        back_button = Button(text="Back to Physical Well-being", size_hint_y=None, height=50, 
                             background_normal='', background_color = (1, 1, 0.733, 1),color=(0.172, 0.373, 0.176, 1))
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

    
if __name__ == "_main_":
    HOPEBRIDGE().run()

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                        UserName TEXT NOT NULL UNIQUE,
                        Password TEXT NOT NULL,
                        Email TEXT NOT NULL UNIQUE,
                        InterestOption TEXT CHECK (InterestOption IN ('Volunteer', 'Donator'))
                    )''')
    conn.commit()
    conn.close()

# Home Screen with Sign In and Sign Up buttons
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        sign_in_btn = Button(text='Sign In', size_hint=(1, 0.5))
        sign_in_btn.bind(on_press=self.go_to_signin)
        layout.add_widget(sign_in_btn)

        sign_up_btn = Button(text='Sign Up', size_hint=(1, 0.5))
        sign_up_btn.bind(on_press=self.go_to_signup)
        layout.add_widget(sign_up_btn)

        self.add_widget(layout)

    def go_to_signin(self, instance):
        self.manager.current = 'Sign-In'

    def go_to_signup(self, instance):
        self.manager.current = 'Sign-Up'

# Sign In Screen
class SignInScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Username'))
        self.username_input = TextInput(multiline=False)
        layout.add_widget(self.username_input)

        layout.add_widget(Label(text='Password'))
        self.password_input = TextInput(password=True, multiline=False)
        layout.add_widget(self.password_input)

        signin_btn = Button(text='Sign-In')
        signin_btn.bind(on_press=self.validate_signin)
        layout.add_widget(signin_btn)

        self.message = Label(text='')
        layout.add_widget(self.message)

        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.go_back_home)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def validate_signin(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT InterestOption FROM Users WHERE UserName=? AND Password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            if user[0] == 'Volunteer':
                self.manager.current = 'Volunteer'
            else:
                self.manager.current = 'UserApp'
        else:
            self.message.text = 'Invalid credentials!'
            self.message.color = (1, 0, 0, 1)

    def go_back_home(self, instance):
        self.manager.current = 'home'

# Sign Up Screen
class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Username'))
        self.username_input = TextInput(multiline=False)
        layout.add_widget(self.username_input)

        layout.add_widget(Label(text='Password'))
        self.password_input = TextInput(password=True, multiline=False)
        layout.add_widget(self.password_input)

        layout.add_widget(Label(text='Email Address'))
        self.email_input = TextInput(multiline=False)
        layout.add_widget(self.email_input)

        self.interest_label = Label(text="Select Interest")
        layout.add_widget(self.interest_label)

        self.volunteer_radio = ToggleButton(text='Volunteer', group='interest', state='down')
        self.donator_radio = ToggleButton(text='Donator', group='interest')

        layout.add_widget(self.volunteer_radio)
        layout.add_widget(self.donator_radio)

        signup_btn = Button(text='Sign Up')
        signup_btn.bind(on_press=self.register_user)
        layout.add_widget(signup_btn)

        self.message = Label(text='')
        layout.add_widget(self.message)

        back_btn = Button(text='Back')
        back_btn.bind(on_press=self.go_back_home)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def register_user(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        email = self.email_input.text
        interest = 'Volunteer' if self.volunteer_radio.state == 'down' else 'Donator'

        if username and password and email:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE UserName=?", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                cursor.execute("UPDATE Users SET Password=?, Email=?, InterestOption=? WHERE UserName=?",
                               (password, email, interest, username))
            else:
                cursor.execute("INSERT INTO Users (UserName, Password, Email, InterestOption) VALUES (?, ?, ?, ?)",
                               (username, password, email, interest))
            
            conn.commit()
            conn.close()
            self.manager.current = 'Sign-In'
        else:
            self.message.text = 'Please fill in all fields.'
            self.message.color = (1, 0, 0, 1)

    def go_back_home(self, instance):
        self.manager.current = 'home'

# Main Menu Screen (for Donators)
class UserApp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        title_label = Label(text="Choose an Option", font_size=32, size_hint=(1, 0.3))
        layout.add_widget(title_label)

        button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.5))

        buttons = [
            ("Mental Wellbeing", "mental_wellbeing_btn"),
            ("Self Donate", ),
            ("Donate Through Volunteers", self.open_donate_through_volunteers)
        ]

        for text, _ in buttons:
            btn = Button(text=text, size_hint=(None, None), height=40, width=250)
            btn.background_color = (1, 1, 0.733, 1)
            btn.color = (0.172, 0.373, 0.176, 1)
            button_layout.add_widget(btn)

        layout.add_widget(button_layout)
        self.add_widget(layout)

        def donate_by_self(self, instance):
         # Navigate to the donation page (where user can donate by themselves)
         self.show_donation_popup() 
       def open_donate_through_volunteers(self, instance):
         from hopebridge_app import HOPEBRIDGE  # Import the HopeBridge app class
         HOPEBRIDGE().run()
 
       def open_mental_wellbeing(self, instance):
          # This will call the HopeBridgeApp (Mental Wellbeing App) when the button is pressed
          from hopebridge_app import HopeBridgeApp  # Import the app
          HopeBridgeApp().run()  # Run the app

# Volunteer Screen
class VolunteerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = get_color_from_hex('#87bb55')
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        title_label = Label(text="Choose a Volunteering Option", font_size=dp(25), halign='center', valign='center')
        layout.add_widget(title_label)

        button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.4))
        button_layout.add_widget(Button(text="Mental Wellbeing"))
        button_layout.add_widget(Button(text="Volunteer to Give Donations", ))
        button_layout.add_widget(Button(text="Volunteer to Collect Donations", on_press=self.volunteer_to_collect_donations))
        layout.add_widget(button_layout)

        self.add_widget(layout)

         def volunteer_to_collect_donations(self, instance):
          LocationTimeApp().run()

        def open_mental_wellbeing(self, instance):
          # This will call the HopeBridgeApp (Mental Wellbeing App) when the button is pressed
          from hopebridge_app import HopeBridgeApp  # Import the app
          HopeBridgeApp().run()  # Run the app

# Main App Class
class LoginApp(App):
    def build(self):
        init_db()
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SignInScreen(name='Sign-In'))
        sm.add_widget(SignUpScreen(name='Sign-Up'))
        sm.add_widget(UserApp(name='UserApp'))
        sm.add_widget(VolunteerScreen(name='Volunteer'))
        return sm

if __name__ == '__main__':
    LoginApp().run()

class DonationApp(App):
    def build(self):
        self.load_data()
        self.screen_manager = ScreenManager()

        # User Credentials Screen
        user_credentials_screen = UserCredentialsScreen(self, name='user_credentials')
        self.screen_manager.add_widget(user_credentials_screen)

        # Set background color for all screens
        Window.clearcolor = (0.533, 0.733, 0.333, 1)

        # Main Screen
        main_layout = BoxLayout(orientation='vertical')
        
        # Existing buttons
        add_donation_button = Button(text='Add Donation', size_hint=(1, 0.1))
        add_donation_button.bind(on_press=self.add_donation)
        main_layout.add_widget(add_donation_button)

        update_button = Button(text='Update Donation', size_hint=(1, 0.1))
        update_button.bind(on_press=self.show_update_donations)
        main_layout.add_widget(update_button)

        update_user_credentials_button = Button(text='Update User Credentials', size_hint=(1, 0.1))
        update_user_credentials_button.bind(on_press=self.show_update_user_credentials)
        main_layout.add_widget(update_user_credentials_button)

        # Add "Donate by Self" button
        donate_by_self_button = Button(text='Donate by Self', size_hint=(1, 0.1))
        donate_by_self_button.bind(on_press=self.donate_by_self)
        main_layout.add_widget(donate_by_self_button)

        exit_button = Button(text='Exit', size_hint=(1, 0.1))
        exit_button.bind(on_press=self.exit_app)
        main_layout.add_widget(exit_button)

        self.main_screen = Screen(name='main')
        self.main_screen.add_widget(main_layout)
        self.screen_manager.add_widget(self.main_screen)

        self.screen_manager.current = 'user_credentials'  # Start with user credentials
        return self.screen_manager

    def donate_by_self(self, instance):
        # Navigate to the donation page (where user can donate by themselves)
        self.show_donation_popup()  # This will trigger the donation entry popup

    def exit_app(self, instance):
        # Switch to the user credentials screen
        self.screen_manager.current = 'user_credentials'

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
from kivy.core.window import Window

class LocationTimeApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Set background color for the entire app
        Window.clearcolor = (0.533, 0.733, 0.333, 1)
        self.add_widget(Label(text='Choose Location Entry Method:', size_hint=(1, 0.1)))
        
        self.manual_toggle = ToggleButton(text='Manual Entry', group='location', size_hint=(1, 0.1))
        self.manual_toggle.bind(on_press=self.toggle_manual_entry)
        self.add_widget(self.manual_toggle)
        
        self.gps_toggle = ToggleButton(text='Use GPS', group='location', state='down', size_hint=(1, 0.1))
        self.gps_toggle.bind(on_press=self.toggle_manual_entry)
        self.add_widget(self.gps_toggle)
        
        self.location_input = TextInput(hint_text='Enter Address Manually', size_hint=(1, 0.1), disabled=True)
        self.add_widget(self.location_input)
        
        self.gps_button = Button(text='Get GPS Location', size_hint=(1, 0.1), background_color=(1, 1, 0.733, 1), color=(0.172, 0.373, 0.176, 1))
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
        
        self.time_button = Button(text='Pick Time', size_hint=(1, 0.1), background_color=(1, 1, 0.733, 1), color=(0.172, 0.373, 0.176, 1))
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

    def exit_app(self, instance):
        # Switch to the user credentials screen
        self.screen_manager.current = 'user_credentials'

class MyApp(MDApp):
    def build(self):
        return LocationTimeApp()

if __name__ == '__main__':
    MyApp().run()

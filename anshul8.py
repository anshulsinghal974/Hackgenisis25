from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

# Home Screen with Sign In and Sign Up buttons
class HomeScreen(Screen):
    def _init_(self, **kwargs):
        super(HomeScreen, self)._init_(**kwargs)
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
    def _init_(self, **kwargs):
        super(SignInScreen, self)._init_(**kwargs)
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

        if username == 'admin' and password == '1234':
            self.message.text = 'Login successful! 🎉'
            self.message.color = (0, 1, 0, 1)
        else:
            self.message.text = 'Invalid credentials!'
            self.message.color = (1, 0, 0, 1)

    def go_back_home(self, instance):
        self.manager.current = 'home'

# Sign Up Screen
class SignUpScreen(Screen):
    def _init_(self, **kwargs):
        super(SignUpScreen, self)._init_(**kwargs)
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

        self.volunteer_radio = ToggleButton(text='Volunteer', group='interest', state='down')  # Default selected option
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

        if username and password and email:
            self.message.text = f'Account created for {username}! 🎉'
            self.message.color = (0, 1, 0, 1)
        else:
            self.message.text = 'Please fill in all fields.'
            self.message.color = (1, 0, 0, 1)

    def go_back_home(self, instance):
        self.manager.current = 'home'

# Main App Class
class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SignInScreen(name='Sign-In'))
        sm.add_widget(SignUpScreen(name='Sign-Up'))
        return sm

if _name_ == '_main_':
    LoginApp().run()
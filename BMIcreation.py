from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
import os


# ============================================================
# APP SETTINGS
# ============================================================

Window.clearcolor = (0.08, 0.08, 0.08, 1)


# ============================================================
# HELPER FUNCTION
# ============================================================

def load_workout_file(filename):
    """
    Loads a workout plan from a text file included with the app.
    """

    # Android/Kivy packaged files are normally located relative
    # to the application's working directory.
    filepath = os.path.join(os.path.dirname(__file__), filename)

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return (
            "ERROR\n\n"
            f"The workout file '{filename}' could not be found.\n\n"
            "Make sure the file is included with the Android app."
        )


# ============================================================
# QUESTION 1 SCREEN
# ============================================================

class GoalScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(15)
        )

        title = Label(
            text="WORKOUT REGIMEN SELECTOR",
            font_size=dp(26),
            bold=True,
            size_hint_y=None,
            height=dp(70)
        )

        question = Label(
            text="What is your main workout goal?",
            font_size=dp(21),
            size_hint_y=None,
            height=dp(70)
        )

        layout.add_widget(title)
        layout.add_widget(question)

        # Build Muscle
        button1 = Button(
            text="1. Build Muscle",
            font_size=dp(20),
            size_hint_y=None,
            height=dp(60)
        )

        button1.bind(
            on_press=lambda instance: self.select_goal(1)
        )

        # Lose Weight
        button2 = Button(
            text="2. Lose Weight / Burn Fat",
            font_size=dp(20),
            size_hint_y=None,
            height=dp(60)
        )

        button2.bind(
            on_press=lambda instance: self.select_goal(2)
        )

        # Strength & Endurance
        button3 = Button(
            text="3. Strength & Endurance",
            font_size=dp(20),
            size_hint_y=None,
            height=dp(60)
        )

        button3.bind(
            on_press=lambda instance: self.select_goal(3)
        )

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)

        self.add_widget(layout)

    def select_goal(self, goal):

        # Store the answer in the app
        App.get_running_app().goal = goal

        # Move to Question 2
        self.manager.current = "workout_type"


# ============================================================
# QUESTION 2 SCREEN
# ============================================================

class WorkoutTypeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(12)
        )

        title = Label(
            text="Question 2",
            font_size=dp(26),
            bold=True,
            size_hint_y=None,
            height=dp(60)
        )

        question = Label(
            text="What type of workouts do you prefer?",
            font_size=dp(20),
            size_hint_y=None,
            height=dp(70)
        )

        layout.add_widget(title)
        layout.add_widget(question)

        choices = [
            ("A. Weight Training", "A"),
            ("B. Cardio", "B"),
            ("C. Bodyweight Exercises", "C"),
            ("D. A Combination of Everything", "D")
        ]

        for text, value in choices:

            button = Button(
                text=text,
                font_size=dp(18),
                size_hint_y=None,
                height=dp(55)
            )

            button.bind(
                on_press=lambda instance, choice=value:
                self.select_workout_type(choice)
            )

            layout.add_widget(button)

        # Back button
        back_button = Button(
            text="Back",
            font_size=dp(18),
            size_hint_y=None,
            height=dp(50)
        )

        back_button.bind(
            on_press=lambda instance:
            setattr(self.manager, "current", "goal")
        )

        layout.add_widget(back_button)

        self.add_widget(layout)

    def select_workout_type(self, workout_type):

        App.get_running_app().workout_type = workout_type

        self.manager.current = "frequency"


# ============================================================
# QUESTION 3 SCREEN
# ============================================================

class FrequencyScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(12)
        )

        title = Label(
            text="Question 3",
            font_size=dp(26),
            bold=True,
            size_hint_y=None,
            height=dp(60)
        )

        question = Label(
            text="How often do you want to work out?",
            font_size=dp(20),
            size_hint_y=None,
            height=dp(70)
        )

        layout.add_widget(title)
        layout.add_widget(question)

        choices = [
            ("A. 2-3 days per week", "A"),
            ("B. 3-4 days per week", "B"),
            ("C. 5-6 days per week", "C"),
            ("D. Every day", "D")
        ]

        for text, value in choices:

            button = Button(
                text=text,
                font_size=dp(18),
                size_hint_y=None,
                height=dp(55)
            )

            button.bind(
                on_press=lambda instance, choice=value:
                self.select_frequency(choice)
            )

            layout.add_widget(button)

        # Back button
        back_button = Button(
            text="Back",
            font_size=dp(18),
            size_hint_y=None,
            height=dp(50)
        )

        back_button.bind(
            on_press=lambda instance:
            setattr(self.manager, "current", "workout_type")
        )

        layout.add_widget(back_button)

        self.add_widget(layout)

    def select_frequency(self, frequency):

        App.get_running_app().frequency = frequency

        # Generate the workout plan
        self.manager.get_screen("plan").display_plan()

        # Go to final screen
        self.manager.current = "plan"


# ============================================================
# WORKOUT PLAN SCREEN
# ============================================================

class PlanScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(10)
        )

        title = Label(
            text="YOUR WORKOUT PLAN",
            font_size=dp(25),
            bold=True,
            size_hint_y=None,
            height=dp(60)
        )

        main_layout.add_widget(title)

        # Scrollable workout plan
        scroll = ScrollView()

        self.plan_label = Label(
            text="",
            font_size=dp(17),
            halign="left",
            valign="top",
            size_hint_y=None,
            padding=(dp(10), dp(10))
        )

        # Allow the label to grow vertically
        self.plan_label.bind(
            texture_size=self.plan_label.setter("size")
        )

        scroll.add_widget(self.plan_label)

        main_layout.add_widget(scroll)

        # Start Over button
        restart_button = Button(
            text="START OVER",
            font_size=dp(19),
            size_hint_y=None,
            height=dp(55)
        )

        restart_button.bind(
            on_press=lambda instance:
            setattr(self.manager, "current", "goal")
        )

        main_layout.add_widget(restart_button)

        self.add_widget(main_layout)

    def display_plan(self):

        app = App.get_running_app()

        goal = app.goal

        # ----------------------------------------------------
        # Select workout file based on Question 1
        # ----------------------------------------------------

        if goal == 1:

            filename = "build_muscle.txt"

        elif goal == 2:

            filename = "loseweightburnfat.txt"

        elif goal == 3:

            # IMPORTANT:
            # Upload the Strength & Endurance file before
            # using this option in the final Android build.

            filename = "Strenghth&endursnce.txt"

        else:

            self.plan_label.text = "Invalid workout goal."

            return

        # Load selected workout plan
        workout_plan = load_workout_file(filename)

        # Display the workout plan
        self.plan_label.text = workout_plan


# ============================================================
# MAIN ANDROID APP
# ============================================================

class WorkoutApp(App):

    # Store answers
    goal = None
    workout_type = None
    frequency = None

    def build(self):

        # Create screen manager
        screen_manager = ScreenManager()

        # Add all screens
        screen_manager.add_widget(
            GoalScreen(name="goal")
        )

        screen_manager.add_widget(
            WorkoutTypeScreen(name="workout_type")
        )

        screen_manager.add_widget(
            FrequencyScreen(name="frequency")
        )

        screen_manager.add_widget(
            PlanScreen(name="plan")
        )

        # Start with Question 1
        screen_manager.current = "goal"

        return screen_manager


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":
    WorkoutApp().run()

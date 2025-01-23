class DietFitnessAgent:
    def collect_user_inputs(self):
        print("=== Create Your Profile ===")
        user_data = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "gender": input("Enter your gender (Male/Female/Other): ").capitalize(),
            "weight": float(input("Enter your weight (kg): ")),
            "height": float(input("Enter your height (cm): ")),
            "activity_level": input("What is your activity level? (Sedentary/Lightly Active/Moderately Active/Very Active): ").capitalize(),
            "medical_conditions": input("Do you have any medical conditions? (e.g., diabetes, hypertension, PCOS, pregnancy): "),
            "allergies": input("Do you have any allergies? (e.g., nuts, gluten, dairy): "),
            "meals_per_day": int(input("How many meals do you eat per day? (e.g., 3 meals, 5 small meals): ")),
            "cooking_preferences": input("What are your cooking preferences? (Home-cooked/Ready-to-eat/Mix): ").capitalize(),
            "stress_levels": input("What are your stress levels? (Low/Medium/High): ").capitalize(),
            "emotional_eating": input("Do you have any emotional eating habits? (e.g., stress eating, binge eating): "),
            "state": input("Which Indian state are you from? (e.g., Tamil Nadu, Punjab, Gujarat): ").capitalize(),
            "diet_duration": input("How long do you need the diet plan for? (e.g., 1 week, 2 weeks, 1 month, custom days): ").lower(),
            "dietary_preference": input("What is your dietary preference? (Vegetarian/Non-Vegetarian/Non-Vegetarian with exceptions): ").capitalize(),
            "dietary_exceptions": input("Are there any specific foods you avoid? (e.g., no beef, no pork): ") if "exceptions" in input else "",
        }
        return user_data
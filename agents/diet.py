import google.generativeai as genai

class GeminiAPIAgent:
    def __init__(self):
        """Initialize the Gemini API."""
        self.model = genai.GenerativeModel('gemini-pro')  # Use the free-tier model

    def generate_diet_plan(self, user_data):
        """Generate a personalized diet plan based on user data."""
        prompt = f"""
        Create a personalized diet plan for the following user:
        - Name: {user_data.get("name", "User")}
        - Age: {user_data.get("age", "N/A")}
        - Gender: {user_data.get("gender", "N/A")}
        - Weight: {user_data.get("weight", "N/A")} kg
        - Height: {user_data.get("height", "N/A")} cm
        - Activity Level: {user_data.get("activity_level", "N/A")}
        - Medical Conditions: {user_data.get("medical_conditions", "None")}
        - Allergies: {user_data.get("allergies", "None")}
        - Meal Preferences: {user_data.get("meals_per_day", "N/A")} meals per day, {user_data.get("cooking_preferences", "N/A")} cooking.
        - Stress Levels: {user_data.get("stress_levels", "N/A")}
        - Emotional Eating Habits: {user_data.get("emotional_eating", "N/A")}
        - State: {user_data.get("state", "N/A")}
        - Diet Duration: {user_data.get("diet_duration", "1 week")}
        - Dietary Preference: {user_data.get("dietary_preference", "N/A")}
        - Dietary Exceptions: {user_data.get("dietary_exceptions", "None")}

        Provide a {user_data.get("diet_duration", "1 week")} diet plan with:
        - Breakfast, lunch, dinner, and snacks.
        - Portion sizes and nutritional breakdown (calories, proteins, carbs, fats, vitamins, etc.).
        - Focus on regional cuisine from {user_data.get("state", "India")}.
        - Respect dietary preferences: {user_data.get("dietary_preference", "N/A")} and exceptions: {user_data.get("dietary_exceptions", "None")}.

        Format the diet plan in a table with the following columns:
        - Day
        - Meal Type (Breakfast, Lunch, Dinner, Snacks)
        - Meal Item
        - Portion Size
        - Calories
        - Proteins (g)
        - Carbs (g)
        - Fats (g)
        - Vitamins
        - Other Nutrients

        Do not include cooking instructions. Be precise and detailed about the nutritional values.
        """
        
        # Generate the diet plan using Gemini API
        response = self.model.generate_content(prompt)
        return response.text
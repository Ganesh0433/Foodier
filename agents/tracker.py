from utils.health import HealthUtils

class TrackerAnalyzerAgent:
    def collect_daily_logs(self, logs_data):
        """Collect daily logs from the request JSON payload."""
        if not logs_data:
            return None  # No logs provided

        logs = {
            "weight": logs_data.get("weight"),
            "water_intake": logs_data.get("water_intake"),
            "exercise": logs_data.get("exercise", "No").capitalize(),
            "diet_adherence": logs_data.get("diet_adherence", "No").capitalize(),
        }
        return logs

    def analyze_progress(self, logs, user_data):
        """Analyze daily logs and provide feedback."""
        if not logs:
            return {"message": "No logs found. Please enter today's logs or exit."}

        print("\n=== Progress Analysis ===")
        
        # Check weight progress
        current_weight = logs.get("weight")
        initial_weight = user_data.get("weight")
        if current_weight and initial_weight:
            weight_change = current_weight - initial_weight
            if weight_change < 0:
                print(f"Great job! You've lost {abs(weight_change):.2f} kg.")
            elif weight_change > 0:
                print(f"Be careful! You've gained {abs(weight_change):.2f} kg.")
            else:
                print("Your weight has remained the same.")

        # Check water intake
        water_intake = logs.get("water_intake")
        hydration_goal = user_data.get("hydration_goals", 2.5)  # Default goal: 2.5 liters
        if water_intake:
            if water_intake >= hydration_goal:
                print("You've met your daily hydration goal. Well done!")
            else:
                print(f"Drink more water! You're {hydration_goal - water_intake:.2f} liters short of your goal.")

        # Check exercise adherence
        exercise = logs.get("exercise")
        if exercise == "Yes":
            print("You followed your exercise routine today. Keep it up!")
        else:
            print("You missed your exercise routine today. Try to stay consistent!")

        # Check diet adherence
        diet_adherence = logs.get("diet_adherence")
        if diet_adherence == "Yes":
            print("You followed your diet plan today. Great work!")
        else:
            print("You strayed from your diet plan today. Stay focused!")

        # Calculate BMI and provide health insights
        bmi, bmi_category = HealthUtils.calculate_bmi(user_data.get("weight"), user_data.get("height"))
        print(f"\nYour BMI is {bmi:.1f}, which is categorized as {bmi_category}.")

        return {"message": "Progress analyzed successfully!", "bmi": bmi, "bmi_category": bmi_category}
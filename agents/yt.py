from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
from utils.health import HealthUtils

# Load environment variables
load_dotenv()

class YouTubeRecommenderAgent:
    def __init__(self):
        """Initialize the YouTube API with the API key from the environment."""
        api_key = os.getenv("YOUTUBE_API_KEY")
        if not api_key:
            raise ValueError("Please set the YOUTUBE_API_KEY in the .env file.")
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def recommend_videos(self, user_data):
        """Fetch exercise videos based on user data."""
        query = f"exercise for {user_data.get('activity_level', 'general fitness')}"

        # Customize query based on BMI and health conditions
        bmi, bmi_category = HealthUtils.calculate_bmi(user_data.get("weight"), user_data.get("height"))
        if "pregnant" in user_data.get("medical_conditions", "").lower():
            query += " safe pregnancy exercises"
        elif bmi_category == "Obese":
            query += " for obese individuals"
        elif bmi_category == "Underweight":
            query += " for underweight individuals"
        elif "thin hands" in user_data.get("physical_attributes", "").lower():
            query += " for strengthening thin hands"
        elif "fat chest" in user_data.get("physical_attributes", "").lower():
            query += " for reducing fat chest"

        search_response = self.youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=5  # Limit to 5 results to stay within quota
        ).execute()
        videos = []
        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            video_title = search_result['snippet']['title']
            videos.append({
                "id": video_id,
                "title": video_title,
                "url": f"https://www.youtube.com/watch?v={video_id}"
            })
        return videos
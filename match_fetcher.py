import requests
from datetime import datetime

API_URL = "YOUR_MATCH_API_ENDPOINT"

def get_today_match():
    response = requests.get(API_URL)
    data = response.json()

    today = datetime.utcnow().date()

    for match in data["matches"]:
        match_date = datetime.fromisoformat(match["start_time"]).date()

        if match_date == today:
            return {
                "team1": match["team1"],
                "team2": match["team2"],
                "status": match["status"],
                "score1": match.get("score1"),
                "score2": match.get("score2")
            }

    return None

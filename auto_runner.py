import requests
import os
from generate_preview import generate_preview
from generate_result import generate_result
from telegram_post import send_telegram
from facebook_post import post_facebook

API_KEY = os.getenv("CRICKET_API_KEY")
SERIES = "T20 World Cup"

def get_match_status():
    data = requests.get(
        f"https://api.cricketdata.org/v1/matches?apikey={API_KEY}"
    ).json().get("data", [])

    for m in data:
        if SERIES.lower() in m.get("series","").lower():
            return m.get("status","").lower()

    return None

def main():
    status = get_match_status()

    if status == "upcoming":
        result = generate_preview()

    elif status == "completed":
        result = generate_result()

    else:
        print("No valid match status today")
        return

    if not result:
        return

    image_path, caption = result

    send_telegram(image_path, caption)
    post_facebook(image_path, caption)

if __name__ == "__main__":
    main()

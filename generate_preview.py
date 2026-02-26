import requests
import os
from jinja2 import Environment, FileSystemLoader
from html_to_image import convert

API_KEY = os.getenv("CRICKET_API_KEY")
SERIES = "T20 World Cup"

def generate_preview():
    data = requests.get(
        f"https://api.cricketdata.org/v1/matches?apikey={API_KEY}"
    ).json().get("data", [])

    upcoming = [
        m for m in data
        if SERIES.lower() in m.get("series","").lower()
        and m.get("status","").lower() == "upcoming"
    ]

    upcoming.sort(key=lambda x: x.get("date",""))

    if not upcoming:
        print("No upcoming match found")
        return None

    match = upcoming[0]

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("preview.html")

    html_content = template.render(match=match)

    html_path = "output/html/preview.html"
    png_path = "output/images/preview.png"

    os.makedirs("output/html", exist_ok=True)
    os.makedirs("output/images", exist_ok=True)

    with open(html_path, "w") as f:
        f.write(html_content)

    convert(html_path, png_path)

    print("Preview generated")

    return png_path, f"{match['team_a']} vs {match['team_b']} – Match Preview 🏏"

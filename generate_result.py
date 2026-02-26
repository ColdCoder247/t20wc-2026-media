import requests
import os
from jinja2 import Environment, FileSystemLoader
from html_to_image import convert

API_KEY = os.getenv("CRICKET_API_KEY")
SERIES = "T20 World Cup"

def generate_result():
    data = requests.get(
        f"https://api.cricketdata.org/v1/matches?apikey={API_KEY}"
    ).json().get("data", [])

    completed = [
        m for m in data
        if SERIES.lower() in m.get("series","").lower()
        and m.get("status","").lower() == "completed"
    ]

    completed.sort(key=lambda x: x.get("date",""), reverse=True)

    if not completed:
        print("No completed match found")
        return None

    match = completed[0]

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("result.html")

    html_content = template.render(match=match)

    html_path = "output/html/result.html"
    png_path = "output/images/result.png"

    os.makedirs("output/html", exist_ok=True)
    os.makedirs("output/images", exist_ok=True)

    with open(html_path, "w") as f:
        f.write(html_content)

    convert(html_path, png_path)

    print("Result generated")

    return png_path, f"{match['team_a']} vs {match['team_b']} – Match Result ✅"

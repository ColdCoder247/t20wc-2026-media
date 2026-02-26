
import requests, os
from jinja2 import Environment, FileSystemLoader
from html_to_image import convert

API_KEY = os.getenv("CRICKET_API_KEY")
SERIES = "T20 World Cup"

data = requests.get(
    f"https://api.cricketdata.org/v1/matches?apikey={API_KEY}"
).json().get("data", [])

matches = [m for m in data if SERIES.lower() in m.get("series","").lower()]
matches.sort(key=lambda x: x.get("date",""))

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("schedule.html")

html_content = template.render(matches=matches[:12])

html_path = "output/html/schedule.html"
png_path = "output/images/schedule.png"

with open(html_path, "w") as f:
    f.write(html_content)

convert(html_path, png_path)

print("Schedule generated")

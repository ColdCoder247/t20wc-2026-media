from match_fetcher import get_today_match
from generate_preview import generate_preview
from generate_result import generate_result
from telegram_post import send_telegram
from facebook_post import post_facebook

def main():
    match = get_today_match()

    if not match:
        print("No match today.")
        return

    team1 = match["team1"]
    team2 = match["team2"]
    status = match["status"]

    if status == "not_started":
        image = generate_preview(team1, team2)
        caption = f"{team1} vs {team2} – Match Preview 🏏"

    elif status == "live":
        image = generate_preview(team1, team2)
        caption = f"{team1} vs {team2} – Live Now 🔥"

    elif status == "ended":
        image = generate_result(match)
        caption = f"{team1} vs {team2} – Match Result ✅"

    else:
        return

    send_telegram(image, caption)
    post_facebook(image, caption)

if __name__ == "__main__":
    main()

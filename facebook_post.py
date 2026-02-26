import requests
import os

PAGE_ID = os.getenv("FB_PAGE_ID")
ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")

def post_facebook(image_path, caption):
    url = f"https://graph.facebook.com/{PAGE_ID}/photos"

    with open(image_path, "rb") as img:
        requests.post(
            url,
            files={"source": img},
            data={
                "caption": caption,
                "access_token": ACCESS_TOKEN
            }
        )

# The Spotlight API URL was extracted from the following Github repository:
# https://github.com/ORelio/Spotlight-Downloader

import requests
import json

spotlight_url = "https://arc.msn.com/v3/Delivery/Cache?pid=209567&fmt=json&rafb=0&ua=WindowsShellClient%2F0&disphorzres=9999&dispvertres=9999&lo=80217&pl=en-US&lc=en-US&ctry=us"

def request_data(url):
    response = requests.get(url)
    return response.text

def get_random_spotlight_image():
    data = request_data(spotlight_url)
    json_data = json.loads(data)
    inner_json = json.loads(json_data["batchrsp"]["items"][0]["item"])
    image_url = inner_json['ad']['image_fullscreen_001_landscape']['u']
    
    return image_url

# This code is based on the answers for the following stackoverflow question:
# https://stackoverflow.com/questions/10639914/is-there-a-way-to-get-bings-photo-of-the-day

import requests
import json

bing_images_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8"

class BingImage:
    def __init__(self,title,rights,url):
        self.title = title
        self.rights = rights
        self.url = url

def request_data(url):
    response = requests.get(url)
    return response.text

def get_bing_images_of_the_day():
    data = request_data(bing_images_url)
    json_data = json.loads(data)
    images = json_data["images"]
    images_list = []
    for image in images:
        bing_image = BingImage(image["title"],
                               image["copyright"],
                               "http://www.bing.com" + image["url"])
        images_list.append(bing_image)
    return images_list


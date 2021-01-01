# This code is based on one of the comments of the following reddit submission:
# https://www.reddit.com/r/TheoryOfReddit/comments/7ktxi3/reddit_question_is_there_a_way_to_determine/

import requests
import json

url_format = "https://api.pushshift.io/reddit/search/submission/?subreddit={}&metadata=true&size=0"

def _get_metadata_json(subreddit: str):
    data = requests.get(url_format.format(subreddit)).text
    json_object = json.loads(data)
    return json_object
def get_submissions_count(subreddit: str):
    json_object = _get_metadata_json(subreddit)
    return json_object["metadata"]["total_results"]

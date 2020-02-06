#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'user-agent': 'python/com.request:v1.0.0 (by /u/sagude23)'
    }

    req = requests.get(url, headers=headers)
    if req.status_code == 404:
        return 0

    req_json = req.json()
    subscribers = req_json["data"]
    num_subscribers = 0
    for key in subscribers:
        if key == "subscribers":
            num_subscribers = subscribers[key]

    return num_subscribers

#!/usr/bin/python3
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        'user-agent': 'python/com.request:v1.0.0 (by /u/sagude23)'
    }

    req = requests.get(url, headers=headers)

    if req.status_code == 404:
        print(None)
    else:
        req = req.json()
        req_items = req.get("data").get("children")
        for i in range(len(req_items)):
            print(req_items[i]["data"]["title"])

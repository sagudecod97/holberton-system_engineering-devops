#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=''):
    if after is None:
        return hot_list

    headers = {
        'user-agent': 'python/com.request:v1.0.0 (by /u/sagude23)'
    }
    params = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 404:
        return None

    req = req.json()
    after = req.get('data').get('after')
    hot_list = recurse(subreddit, hot_list, after)

    req_body = req.get('data').get('children')
    for item in req_body:
        hot_list.append(item["data"]["title"])

    return hot_list

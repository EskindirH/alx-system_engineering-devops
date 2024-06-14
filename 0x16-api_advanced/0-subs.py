#!/usr/bin/python3
"""
Query that returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    u_agent = 'Custom-agent'

    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0

    dic = res.json()

    if 'data' not in dic:
        return 0

    if 'subscribers' not in dic.get('data'):
        return 0

    return res.json()['data']['subscribers']

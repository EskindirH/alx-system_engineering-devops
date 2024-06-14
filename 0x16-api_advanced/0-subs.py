#!/usr/bin/python3
"""Function that queries subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers.
    Args:
        subreddit: subreddits.

    Returns:
        int: number of subscribers.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linx:0x16-api_advanced:v1.0.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")

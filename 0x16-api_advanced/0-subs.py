#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
import sys


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
  
    if response.status_code == 200:
        return (resronse.json().get("data").get("subscribers"))
    return (0)


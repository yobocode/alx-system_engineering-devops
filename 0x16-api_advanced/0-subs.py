#!/usr/bin/python3
"""A module containing function for working with number of subscribers
"""
import requests


URL = 'https://www.reddit.com'


def number_of_subscribers(subreddit):
    """Retrives the number of subscibers in a given subreddit
    """
    headers = {
            'Accept': 'application/json',
            'User-Agent': ' '.join([
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'AppleWebKit/537.36 (KHTML, like Gecko)',
                'Chrome/112.0.0.0',
                'Safari/537.36'
                ])
            }
    result = requests.get(
            '{}/r/{}/about/.json'.format(URL, subreddit),
            headers=headers,
            allow_redirects=False
            )
    if result.status_code == 200:
        return result.json()['data']['subscribers']
    return 0

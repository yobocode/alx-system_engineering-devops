#!/usr/bin/python3
'''A module containing function for working with reddit api.
'''
import requests


URL = 'https://www.reddit.com'


def top_ten(subreddit):
    '''Retrives the tittle of top ten posts of the given subreddit.
    '''
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
            '{}/r/{}/hot.json?sort=top&limit=10'.format(URL, subreddit),
            headers=headers,
            allow_redirects=False
            )
    if result.status_code == 200:
        posts = result.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)

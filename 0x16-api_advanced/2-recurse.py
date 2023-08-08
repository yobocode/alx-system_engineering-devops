#!/usr/bin/python3
"""A module conataing fuction for working with reddit api.
"""
import requests


URL = 'https://www.reddit.com'


def recurse(subreddit, hot_list=[], counts=0, after=''):
    '''Retrives a list of hot posts from the given subreddit.
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
    limit = 50
    result = requests.get(
            '{}/r/{}/hot.json?sort=top&limit={}&count={}&after={}'.format(
                URL,
                subreddit,
                limit,
                counts,
                after),
            headers=headers,
            allow_redirects=False
            )
    if result.status_code == 200:
        posts = result.json()['data']['children']
        count = len(posts)
        hot_list.extend(list(map(lambda post: post['data']['title'], posts)))
        if count >= limit and result.json()['data']['after']:
            return recurse(subreddit, hot_list, counts + count,
                           result.json()['data']['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None

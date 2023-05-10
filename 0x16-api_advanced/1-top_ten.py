#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests
import sys

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    headers = {"User-Agent": 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False, 
                           params=parameters)
    if response.status_code == 200:
        titles = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
     else:
        print(None)

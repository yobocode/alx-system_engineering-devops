#!/usr/bin/python3
"""A module containing functions for working with the Reddit API.
"""
import requests


def hist_sort(hist={}):
    '''Sorts and prints the given histogram.
    '''
    hist = list(filter(lambda tup: tup[1], hist))
    hist_dict = {}
    for item in hist:
        if item[0] in hist_dict:
            hist_dict[item[0]] += item[1]
        else:
            hist_dict[item[0]] = item[1]
    hist = list(hist_dict.items())
    hist.sort(
        key=lambda tup: tup[0],
        reverse=False
    )
    hist.sort(
        key=lambda tup: tup[1],
        reverse=True
    )
    printable_str = '\n'.join(list(map(
        lambda tup: '{}: {}'.format(tup[0], tup[1]),
        hist
    )))
    if printable_str:
        print(printable_str)


def count_words(subreddit, word_list, hist=[], count=0, after=''):
    '''
    Counts the number of times each word in a given wordlist
    occurs in a given subreddit.
    '''
    headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    sort = 'hot'
    limit = 30
    result = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            'https://www.reddit.com',
            subreddit,
            sort,
            limit,
            count,
            after
        ),
        headers=headers,
        allow_redirects=False
    )
    if not hist:
        word_list = list(map(lambda word: word.lower(), word_list))
        hist = list(map(lambda word: (word, 0), word_list))
    if result.status_code == 200:
        data = result.json()['data']
        posts = data['children']
        titles = list(map(lambda post: post['data']['title'], posts))
        hist = list(map(
            lambda tup: (tup[0], tup[1] + sum(list(map(
                lambda txt: txt.lower().split().count(tup[0]),
                titles
            )))),
            hist
        ))
        if len(posts) >= limit and data['after']:
            count_words(
                subreddit,
                word_list,
                hist,
                count + len(posts),
                data['after']
            )
        else:
            hist_sort(hist)
    else:
        return

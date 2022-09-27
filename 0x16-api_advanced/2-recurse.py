#!/usr/bin/python3
'''function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''Main function'''

    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after, 'limit': 100}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code > 300:
        return None
    all = res.json()['data']['children']
    after = res.json()['data']['after']

    for elements in all:
        hot_list.append(elements['data']['title'])

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list

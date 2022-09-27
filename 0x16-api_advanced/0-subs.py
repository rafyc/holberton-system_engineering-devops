#!/usr/local/bin/python3
'''function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
'''
import requests

headers = {
    'User-Agent': 'My User Agent 1.0'
}


def number_of_subscribers(subreddit):
    '''Main function'''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 404:
        return (res.json()['data']['subscribers'])
    return 0

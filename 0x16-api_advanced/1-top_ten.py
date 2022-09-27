#!/usr/local/bin/python3
'''function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
'''
import requests

headers = {
    'User-Agent': 'My User Agent 1.0'
}
params = {'limit': 10}


def top_ten(subreddit):
    '''Main function'''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 404:
        all = (res.json()['data']['children'])
        for elements in all:
            print(elements['data']['title'])
        return
    print(None)

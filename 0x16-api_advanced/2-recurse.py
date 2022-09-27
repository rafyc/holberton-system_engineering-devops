#!/usr/bin/python3
'''function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit'''

import requests


def recurse(subreddit, hot_list=[]):
    '''main function'''


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
        print(all['data']['title'])
        return
    print(None)

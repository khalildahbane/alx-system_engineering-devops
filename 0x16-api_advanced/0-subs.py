import requests
from requests.exceptions import HTTPError

def recurse(subreddit, hot_list=[], after=None):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'
    try:
        response = requests.get(url, headers={'User-agent': 'my-app/0.0.1'})
        response.raise_for_status()
        data = response.json()
        if data['data']['children']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            return recurse(subreddit, hot_list, after)
        else:
            return None
    except HTTPError as http_err:
        if response.status_code == 404:
            return None
        else:
            print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

# Example usage
hot_list = recurse('python')
if hot_list:
    for title in hot_list:
        print(title)
else:
    print('No results found for the given subreddit.')

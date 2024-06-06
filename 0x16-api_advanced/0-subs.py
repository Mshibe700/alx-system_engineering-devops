#!/usr/bin/python3
"""
Module to query the Reddit API and retrieve the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function to query the Reddit API and return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    subscribers = number_of_subscribers(subreddit_name)
    print(f"The number of subscribers of r/{subreddit_name}: {subscribers}")


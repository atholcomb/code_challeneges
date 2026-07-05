#!/usr/bin/python3
# written by: atholcomb
# url_shortenerV2.py

import random

base_url = "https://bit.ly/"

def shortenUrl(url):
    link = ""
    
    for r in range(8):
        chars = random.choice("1234567890abcdefghijklmnopqrstuvwxyz")
        link += chars

    url.replace('https://www', '')
    url.replace('www', '')
    url.replace('https://', '')
    
    return base_url + link + ' -> ' + url


print(shortenUrl("https://www.reddit.com"))
print(shortenUrl("www.reddit.com"))
print(shortenUrl("https://reddit.com"))
print(shortenUrl("reddit.com"))

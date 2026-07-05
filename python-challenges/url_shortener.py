#!/usr/bin/python3
# written by: atholcomb
# url_shortener.py

import random

base_url = "https://bit.ly/"

def shortenUrl(url1):

    link = ""
    for r in range(8):
        chars = random.choice("1234567890abcdefghijklmnopqrstuvwxyz")
        link += chars

    #url = input("Enter url: ")
    url = url1
    if "w." in url:
        ww = url.index("w.")
        #return base_url + link + " -> " + url[ww+2:]
        return base_url + link + " -> " + url
    elif "//" in url:
        ht = url.index("//")
        #return base_url + link + " -> " + url[ht+2:]
        return base_url + link + " -> " + url
    else:
        return base_url + link + " -> " + url

print(shortenUrl("https://www.reddit.com"))
print(shortenUrl("www.reddit.com"))
print(shortenUrl("https://reddit.com"))
print(shortenUrl("reddit.com"))

#!/usr/bin/python3

import pyshorteners
url = input("Enter your url: ")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Success! Your shortened URL is:", s)

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:19:45 2020

@author: AAYUSH MISHRA
"""

import sys
import webbrowser
import bs4
import requests

print('Searching...')

res = requests.get('https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')

openTabs = min(5, len(linkElems))
for i in range(openTabs):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
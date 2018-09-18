#! python3
# lucky.py - OPens serveral Sogou search results.
import requests, sys, webbrowser
from bs4 import BeautifulSoup

print('Sogou...')
url = 'https://www.sogou.com/web?query=' + ' '.join(sys.argv[1:])
print(url)
webbrowser.open(url)
res = requests.get(url)
res.raise_for_status()

# Retrieve top search result links.
soup = BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.rb .pt a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    openUrl = "https://www.sogou.com" + linkElems[i].get('href')
    webbrowser.open(openUrl)
    print(openUrl)


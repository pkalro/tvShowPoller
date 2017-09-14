import ssl
import urllib.request
import re
import json
from bs4 import BeautifulSoup
import webbrowser


chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
ssl._create_default_https_context = ssl._create_unverified_context
headers = { 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0' }


req = urllib.request.Request('https://1337x.to/search/narcos+season+3/1/', headers=headers)

with urllib.request.urlopen(req) as response:
    parsedHtml = BeautifulSoup(response.read(), 'html.parser')
    anchorTags = parsedHtml.findAll('a', attrs={'href': re.compile("^/torrent/")})
    for link in anchorTags[:1]:
        # b = webbrowser.get(using='chrome')
        # b.open(link, new =1)
        # webbrowser.get(chrome_path).open(link)
        # webbrowser.open(link, new=2)
        print(link.get('href'))
# with open('test2.png', 'b+w') as f:
#     f.write(g.read())

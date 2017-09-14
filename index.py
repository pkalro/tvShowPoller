import ssl
import urllib.request
import re
import json
from bs4 import BeautifulSoup
import webbrowser

ssl._create_default_https_context = ssl._create_unverified_context

headers = { 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0' }

file_path = './show_list.json'


def get_show_names(path):
    with open(path, encoding='utf-8') as show_list_file:
        return json.load(show_list_file)

def parse_show_names(show_list):
    def space_replace(show_name): return show_name.replace(" ", "+")
    return list(map(space_replace, show_list))

def get_torrent_urls(show_list):
    torrent_urls = []
    for show_name in show_list:
        req_url = 'https://1337x.to/search/{}/1/'.format(show_name)
        req_raw = urllib.request.Request(req_url, headers = headers)
        with urllib.request.urlopen(req_raw) as response:
            parsedHtml = BeautifulSoup(response.read(), 'html.parser')
            anchorTags = parsedHtml.findAll('a', attrs={'href': re.compile("^/torrent/")})
            torrent_urls.append('https://1337x.to{}'.format(anchorTags[0].get('href'))) # Selecting torrent with max seeds and leechers
    return torrent_urls





show_list = get_show_names(file_path)

s = parse_show_names(show_list)

t = get_torrent_urls(s)

print(t)
# req = urllib.request.Request('https://1337x.to/search/narcos+season+3/1/', headers=headers)

# with urllib.request.urlopen(req) as response:
#     parsedHtml = BeautifulSoup(response.read(), 'html.parser')
#     anchorTags = parsedHtml.findAll('a', attrs={'href': re.compile("^/torrent/")})
#     for link in anchorTags[:1]:
#
#         print(link.get('href'))
# # with open('test2.png', 'b+w') as f:
# #     f.write(g.read())

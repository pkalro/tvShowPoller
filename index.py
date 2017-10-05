import ssl
import urllib.request
import re
import json
from bs4 import BeautifulSoup
import platform
import os

ssl._create_default_https_context = ssl._create_unverified_context

headers = { 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0' }

file_path = './show_list.json'

def parse_request(request, tag, attribute_object):
    with urllib.request.urlopen(request) as response:
        parsedHtml = BeautifulSoup(response.read(), 'html.parser')
        filtered_tags = parsedHtml.findAll(tag, attrs=attribute_object)
        return filtered_tags

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
        torrent_links = parse_request(req_raw, 'a', {'href': re.compile("^/torrent/")})
    return torrent_urls

def get_magnet_links(torrent_links):
    magnet_links = []
    for link in torrent_links:
        request = urllib.request.Request('https://1337x.to{}'.format(link.get('href')), headers = headers)
        magnet_links = parse_request(request, 'a', {'class': "magnet-link" })
    return magnet_links

def open_magnet_links(torrent_urls):
    o = platform.system()
    print(o)
    for torrent in torrent_urls:
        if(o == "Windows"):
            os.startfile(torrent)
        else:
            xdg-open(torrent) #For linux users

show_list = get_show_names(file_path)

s = parse_show_names(show_list)

t = get_torrent_urls(s)

m = get_magnet_links(t)

open_magnet_links(m)

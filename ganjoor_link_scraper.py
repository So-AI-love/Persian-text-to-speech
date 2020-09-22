#https://stackoverflow.com/questions/59347372/how-extract-all-urls-in-a-website-using-beautifulsoup

import requests
from bs4 import BeautifulSoup
import re
import time

source_code = requests.get('https://ganjoor.net/')
soup = BeautifulSoup(source_code.content, 'lxml')
data = []
links = []
url_layers_dept=1066

def remove_duplicates(l): # remove duplicates and unURL string
    for item in l:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            links.append((match.group("url")))


for link in soup.find_all('a', href=True):
    data.append(str(link.get('href')))
flag = True
remove_duplicates(data)
while flag:
    try:
        for link in links:
            for j in soup.find_all('a', href=True):
                temp = []
                source_code = requests.get(link)
                soup = BeautifulSoup(source_code.content, 'lxml')
                temp.append(str(j.get('href')))
                remove_duplicates(temp)

                if len(links) > url_layers_dept: # set limitation to number of URLs
                    break
            if len(links) > url_layers_dept:
                break
        if len(links) > url_layers_dept:
            break
    except Exception as e:
        print(e)
        if len(links) > url_layers_dept:
            break

for url in links:
  print(url)
  with open('links.txt','w+') as f:
    for link in soup.find_all('a'):
        f.write(link.get('href'))
        f.write("\n")

        
# https://stackoverflow.com/questions/63941441/web-scraping-the-audio-and-related-text-form-ganjoor-site-by-colab-as-persian-sp/63967423#63967423
import re

import requests

from bs4 import BeautifulSoup
from shutil import copyfileobj

import sys,os
print(os.path.dirname(os.path.abspath(sys.argv[0])))

myList = []
fp = open('links.txt')
for line in fp.readlines():
    myList.append(line)
fp.close()

num_lines = sum(1 for line in open('links.txt'))


with open('links.txt') as f:
    urls = f.read()
    links = re.findall('"((http)s?://.*?)"', urls)
for url in links:
    print(url[0])

for i in range(num_lines):
    print(myList[i])

for i in range(num_lines):

    url = myList[i].rstrip('\n') # "https://ganjoor.net/hafez/ghazal/sh1/"
    page = requests.get(url).text

    text = BeautifulSoup(page, "html.parser").find_all("div", {"class": "m2"})
    print([t.text.replace("\u200c", "") for t in text])

    pattern = re.compile(r"https://i\.ganjoor\.net/a2?/\d+[-a-z]+?\.mp3")
    audio_tracks = re.findall(pattern, page)
    print(audio_tracks)

    for track in audio_tracks:
        print(f"Fetching track: {track}...")
        with requests.get(track, stream=True) as t, \
                open(track.split("/")[-1], "wb") as a:
            copyfileobj(t.raw, a)

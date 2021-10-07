from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

last_links = soup.find(class_='AlphaNav')
last_links.decompose()

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

# Usar .contents para pegar as tags <a> filhas
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    print(names)
    print(links)

# response = urlopen(url)
# html = response.read()

# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find('h1', id='current-weather-temperature').get_text())
# print(soup.find('span', id='current-weather-city').get_text())
import requests
from bs4 import BeautifulSoup

URL = 'https://hodinky.heureka.cz/casio-a700weg-9a/#'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}

stranka = requests.get(URL, header=header)

soup = BeautifulSoup(stranka.content, 'html.parser')

print(soup.prettify())

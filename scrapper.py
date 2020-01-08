import requests
from bs4 import BeautifulSoup
import re

URL = 'https://hodinky.heureka.cz/casio-a700weg-9a/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}

stranka = requests.get(URL, headers=headers)

soup = BeautifulSoup(stranka.content, 'html.parser')

# print(soup.prettify())

# def count_records(search_word):
#     scrapped_text = soup.get_text()
#     scrapped_lower = scrapped_text.lower()
#
#     word_orig = search_word
#     word_low = word_orig.lower()
#
#     print("The word", word_low, "is present", scrapped_lower.count(word_low), "times in the file.")
#
# count_records("CASIO")
# print(soup)

a = soup.findAll(text=re.compile("Kč"))
print(a)

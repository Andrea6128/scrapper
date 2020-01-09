import requests
from bs4 import BeautifulSoup
import re
import sys
import string

print("Heureka.cz Price Scrapper - (c) 2020 Andrea Petriku")
print("Usage: python scrapper.py <http[s]://<product>.heureka.cz/product-name-as-found-by-google>")
print()

# saves shell argument into URL var
URL = sys.argv[1]

if "http" not in URL or "https" not in URL:
    print("Please enter a valid URL (example: https://website.dk/)")
    sys.exit()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}

stranka = requests.get(URL, headers=headers)
soup = BeautifulSoup(stranka.content, 'html.parser')
vycuc = soup.findAll(text=re.compile("Kč"))

# remove unwanted chars and print product_name
product_name = re.sub(r" od .*$", "", vycuc[0])
print("Product name:", product_name)

# prices start at 3th item in list and end at -1st place
prices = vycuc[3:-1]

# print(vycuc)

new_list = []
for i in range(len(prices)):
    value = prices[i].strip(' Kč')
    new_list.append(value)

# remove xx\xa0 records
for unwanted in new_list:
    if "\xa0" in unwanted:
        new_list.remove(unwanted)

# remove spaces
new_list2 = []
for i in range(len(new_list)):
    a = re.sub(r"\s+", "", new_list[i])
    new_list2.append(a)

print(new_list2)

# remove anything other than prices
rec_index = 0
try:
    for record in new_list2:
        for letter in record:
            for char in range(10):
                end_of_record = 0
                print("letter:", letter, "char:", char)
                if letter == str(char):
                    print("letter:", letter, "char:", char)
                    print("letter == char .. ok")
                    break
                else:
                    break

            print("end of record")
            end_or_record = 1
            print("popping: ", new_list2[rec_index])
            new_list2.pop(rec_index)

    rec_index += 1
except IndexError:
    pass

print(new_list2)

new_list2.sort()
print("The lowest price is:", new_list2[0], "CZK")

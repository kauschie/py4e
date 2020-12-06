from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

counts = 0
tagtype = 'p'
tags = soup(tagtype)
for tag in tags:
    counts += 1
print(f"There were {counts} '<{tagtype}>' tags on this page.")
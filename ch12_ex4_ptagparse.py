from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

# ignore ssl certs

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# read web data and use BeautifulSoup to parse the ugly html

url = input('Enter - ')
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

# print(soup)

nums = list()
spans = soup('span')
for span in spans:
    nums.append(int(span.contents[0]))
print(sum(nums))

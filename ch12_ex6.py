from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl


def get_teh_soup(url):
    print(f"Retrieving: {url}")
    html = urlopen(url, context = ctx).read().decode()
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_link(soup):
    links = soup('a')
    return links[17].get('href')

# ignore ssl certs

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# read web data and use BeautifulSoup to parse the ugly html




for i in range(7):
    if i == 0:
        soup = get_teh_soup(input('Enter - '))
        # print(f"------------------------------------")
        # print("---------------SOUP------------------")
        # print(soup)
        # print('================================')
        # print('----------End of soup ------------')
    else:
        soup = get_teh_soup(newlink)
    newlink = get_link(soup)
print(f"Final link: {newlink}")






# nums = list()
# tagsrch = 'a'
# tags = soup(tagsrch)
# for i in range(len(tags)):
#     link = tag.get('href')
#     print(link)



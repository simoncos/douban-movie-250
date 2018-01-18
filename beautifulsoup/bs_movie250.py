    # -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup


i = 0
while i <= 250:
    fp = urllib.request.urlopen("https://movie.douban.com/top250?start={}".format(i))
    page_bytes = fp.read()
    page_str = page_bytes.decode("utf8")
    page_soup = BeautifulSoup(page_str, 'html.parser')
    for movie in page_soup.find_all('div', {'class':'item'}):
        print('\nTop {}:'.format(movie.find('em').text))
        print(movie.find('span', {'class':'title'}).text)
        print(movie.find('a').attrs['href'])
        print(movie.find_next('div', {'class':'star'}).find('span', {'class':'rating_num'}).text)
        print(movie.find_next('div', {'class':'star'}).find_all()[3].text)
    fp.close()
    i += 25


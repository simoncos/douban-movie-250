import time
import platform
from selenium import webdriver

if platform.system() == 'Windows':
    driver = webdriver.Chrome('C:\\Users\\chromedriver.exe') # download and put chromedriver.exe to this path first
else:
    driver = webdriver.Chrome('./chromedriver')

driver.get('https://movie.douban.com/top250')

while True:
    for info in driver.find_elements_by_xpath('//div[@class="item"]'):
        print(info.find_element_by_xpath('div[@class="pic"]/em').text,
              info.find_element_by_xpath('div[@class="pic"]/a/img').get_attribute('alt'),
              info.find_element_by_xpath('div[@class="pic"]/a').get_attribute('href'),
              info.find_element_by_xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]').text,
              info.find_element_by_xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]').text,
              info.find_element_by_xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span').text)
        # title = info.xpath('div[@class="pic"]/a/img/@alt').extract()
        # print(title)
    next = driver.find_element_by_xpath('//span[@class="next"]/a')
    time.sleep(5)
    next.click()
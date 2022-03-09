# #생활코딩(쿠팡은 가능, 오늘의집은 불가; 아마 동적이냐 정적이냐의 차이일듯)
# import requests
# import re
# from bs4 import BeautifulSoup
#
#
# url = "https://www.coupang.com/np/campaigns/82/components/115573?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=Y&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=115573&rating=0"
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
#
# items = soup.find_all("li", attrs={"class":re.compile("^baby-product renew-badge")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

# #셀레니움
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# driver = webdriver.Chrome('/Users/binkim/Desktop/sparta/mini_10')
# driver.implicitly_wait(3)
#
# driver.get('https://ohou.se/productions/feed?query=%EC%A7%91%EB%93%A4%EC%9D%B4%20%EC%84%A0%EB%AC%BC&search_affect_type=Typing&input_source=productions')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# products = soup.select('body > div.page > div > div.production-feed.container > div:nth-child(3) > div > div')
# for product in products:
#     a = product.select_one('#product-264953 > div.production-item__content > h1 > span.production-item__header__name')
#     if a is not None:
#         name = a.text
#         print(name)
#
# driver.close()

# body > div.page > div > div.production-feed.container > div:nth-child(3) > div > div:nth-child(1)
# body > div.page > div > div.production-feed.container > div:nth-child(3) > div > div:nth-child(2)
# #product-264953 > div.production-item__content > h1 > span.production-item__header__name

# 셀레니움(생활코딩)
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://ohou.se/productions/feed?query=%EC%A7%91%EB%93%A4%EC%9D%B4%20%EC%84%A0%EB%AC%BC&search_affect_type=Typing&input_source=productions"
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
#
# gifts = soup.find_all("div", attrs={"class":"production-feed__item-wrap col-6 col-md-4 col-lg-3"})
# # print(len(gifts))
#
# # with open("gifts.html", "w", encoding="utf8") as f:
# #     f.write(soup.prettify())
#
# for gift in gifts:
#     title = gift.find("span", attrs={"class":"production-item__header__name"}).get_text()
#     print(title)
import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
import ssl
import requests

context = ssl._create_unverified_context()


# 웹페이지 내용 전체 끌어오기
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%A7%84%EC%A3%BC%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(webpage, 'html.parser')
# print(soup)


#일부만 끌어오기
# temps = soup.find('div','temperature_text')
# print(temps)

# temps = soup.find('div','temperature_info')
# print(temps)


# temps = soup.find('div','sort')
# print(temps)


dl_summary = soup.find('dl','summary_list')
# print(dl_summary)
print(dl_summary.text.strip())


# dl_summary = soup.find('div', {"class":"temperature_text"})
# print(dl_summary)


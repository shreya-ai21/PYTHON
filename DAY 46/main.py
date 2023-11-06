import datetime
from bs4 import BeautifulSoup
import requests

day,month,year=input().split()
date=datetime.datetime(int(year),int(month),int(day)).strftime("%Y-%m-%d")

response=requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")

soup=BeautifulSoup(response.text,'html.parser')

# print(soup.find("h3",_class="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"))

first=soup.find("h3",attrs={"id":"title-of-a-story","_class":"c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"})
print(first)

ans=soup.find_all("h3",attrs={"id":"title-of-a-story","class":"c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"})
ans1 = [element.get_text().replace('\n', '').replace('\t', '') for element in ans]
# for item in ans:
#     text1=item.get_text()
#     ans1.append(text1)

print(ans1)

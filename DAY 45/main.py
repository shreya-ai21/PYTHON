from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/').text

soup = BeautifulSoup(response, 'html.parser')

texts = []
links = []
upvotes = [int(i.getText().split()[0])
           for i in soup.find_all(name='span', class_='score')]

articles = soup.find_all(name='a', rel='noreferrer')
for i in articles:
    texts.append(i.getText())
    links.append(i.get('href'))

# print(texts)
# print(links)
# print(upvotes)

ans = max(upvotes)
ans_index = upvotes.index(ans)
print(texts[ans_index])
print(links[ans_index])
print(ans)

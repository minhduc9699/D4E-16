import requests
from bs4 import BeautifulSoup

result = requests.get('https://dantri.com.vn/')
soup = BeautifulSoup(result.text)

div_tag = soup.find('div', {'class': 'highlight-event'})
ul = div_tag.find('ul')
titles_list = ul.find_all('li')
for title in titles_list:
    content = title.find('a')
    print(content.text.strip())
    print(content['href'])
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import webbrowser

search = '작은집'
r = requests.get('http://search.naver.com/search.naver?sm=top_hty&fbm=1&utf8&query=' + search) # 단계 1-2
soup = BeautifulSoup(r.text, 'lxml') #단계 3

for i, li in enumerate(soup.select('div.sp_post ul li dl') + soup.select('div.blog ul li dl')):
    a = li.select('dt a')[0] # 이하 단계  4-5
    print(i+1, a.text, '-', li.select('dd')[1].text, a.attrs['href'])
    print()

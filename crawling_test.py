import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8"
res = requests.get(url)
print(res)
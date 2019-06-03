import requests
from bs4 import BeautifulSoup
from hike import Hike

print("Hello World")
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

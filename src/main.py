import requests
from bs4 import BeautifulSoup
from hike import Hike

hike = Hike("Nice Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"], True)
print(hike)
print("Hello World")
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

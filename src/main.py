import requests
from bs4 import BeautifulSoup
from hike import Hike

hike = Hike("Nice Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"], True)
print(hike)

class ScrapedIndex:
    index_link = "https://www.wta.org/go-outside/hikes"
    index_response = requests.get(index_link)
    print (index_response)
    index_content = BeautifulSoup (index_response.content, "html.parser")
    div = index_content.find(id="search-result-listing")
    for hike_div in div.findChildren ("div"):
        print(hike_div)

print(ScrapedIndex())
import requests
from bs4 import BeautifulSoup
from hike import Hike

class ScrapedIndex:
    def all_hikes(self):
        firp_hikes = []
        index_link = "https://www.wta.org/go-outside/hikes"
        index_response = requests.get(index_link)
        index_content = BeautifulSoup (index_response.content, "html.parser")
        div = index_content.find(id="search-result-listing")
        for hike_div in div.findChildren ("div",{"class":"search-result-item"}):
            hike_name = hike_div.find(class_="listitem-title").find("span").text
            highpoint_div = hike_div.find(class_="hike-highpoint hike-stat")
            elevation = 0
            if highpoint_div:
                elevation = float(highpoint_div.find("span").text)
            length_div = hike_div.find(class_="hike-length hike-stat")
            length = 0
            if length_div:
                length = float(length_div.find("span").text.split()[0])
            firp_hikes.append(Hike(hike_name, 0, 0, elevation, length, [], [], False))
        return firp_hikes

class IndividualScraped:
    def ind_hikes(self):
        pass

    def __init__(self, page_link):
        page_link_response = requests.get(page_link)

p = IndividualScraped ("https://www.wta.org/go-hiking/hikes/thorp-mountain-lookout-via-thorp-creek")

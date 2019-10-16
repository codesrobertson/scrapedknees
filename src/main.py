import requests
from bs4 import BeautifulSoup
from hike import Hike
from serialize import Serializer
from user_input import UserInputParser

HIKE_FILE_PATH = "out/hikes.tsv"
INVALID = "<INVALID>"


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


print("Scraping index page for hikes...")
hikes = ScrapedIndex().all_hikes()
print(f"Writing hikes to file: '{HIKE_FILE_PATH}'")
Serializer(HIKE_FILE_PATH).serialize(hikes)

parser = UserInputParser(INVALID)
print("How long of a hike would you like to take?")
hike_length = INVALID
while hike_length == INVALID:
    hike_length = parser.parse_number_range(input())
    if hike_length == INVALID:
        print("Please enter a valid hike length or range")
print(f"You said you want a hike of length {hike_length}")

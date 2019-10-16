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
    def __init__(self, page_link):
        page_link_response = requests.get(page_link)
        index_content = BeautifulSoup(page_link_response.content, "html.parser")
        lat,long = self.get_lat_long(index_content)
        hike_name = self.get_hike_name(index_content)

    def get_lat_long(self,index_content):
        lat_long = index_content.find(class_="latlong")
        lat_long_spans = lat_long.find_all("span")
        lat = float(lat_long_spans[0].text)
        long = float(lat_long_spans[1].text)
        return (lat,long)

    def get_hike_name(self, index_content):
        hike_name = index_content.find(class_="documentFirstHeading")
        hike_name = hike_name.text
        return (hike_name)

    def get_hike_stats(self, index_content):
        hike_stats = index_content.find(id="hike-stats")
        stats_spans = hike_stats.find_all("span")
        gain = float(stats_spans[0].text)
        high_point = float(stats_spans[1].text)
        return(gain, high_point)

    def get_length(self, index_content):
        length_stat = index_content.find(id="distance")
        distance = length_stat.find_all("span")
        if distance contains "one way", "one-way", "oneway":
            float*2
            return float
        else
            return(distance)
        end

    def properties(self, index_content):
        properties_stats = index_content.find(id="hike-features")
        properties_stats 









IndividualScraped("https://www.wta.org/go-hiking/hikes/thorp-mountain-lookout-via-thorp-creek")

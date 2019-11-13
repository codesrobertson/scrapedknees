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
            hike_link = hike_div.find(class_="listitem-title").attrs["href"]
            firp_hikes.append(hike_link)
        return firp_hikes

class IndividualScraped:
    def __init__(self, page_link):
        page_link_response = requests.get(page_link)
        index_content = BeautifulSoup(page_link_response.content, "html.parser")
        lat,long = self.get_lat_long(index_content)
        hike_name = self.get_hike_name(index_content)
        gain, highpoint = self.get_hike_stats(index_content)
        distance = self.get_length(index_content)
        properties = self.get_properties(index_content)
        permits = self.get_permits(index_content)
        self.hike = Hike(hike_name, lat,long, max(gain, highpoint), distance, properties, permits, False)

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
        hike_stats = index_content.find_all(class_ ="hike-stat")[2]
        stats_spans = hike_stats.find_all("span")
        gain = float(stats_spans[0].text)
        high_point = float(stats_spans[1].text)
        return(gain, high_point)

    def get_length(self, index_content):
        length_stat = index_content.find(id="distance")
        distance = length_stat.find("span").text
        distance_value = float(distance.split()[0])
        if distance in ["one way", "one-way", "oneway"]:
            distance_value*=2
            return distance_value
        else:
            return(distance_value)


    def get_properties(self, index_content):
        properties_stats = index_content.find(id="hike-features")
        properties_features = properties_stats.find_all(class_= "feature")
        attributes = []
        for feature in properties_features:
            attributes.append(feature.attrs["data-title"])
        return(attributes)

    def get_permits(self, index_content):
        permits_stat = index_content.find(class_="alerts-and-conditions")
        permit = permits_stat.find("a").text
        return[permit]











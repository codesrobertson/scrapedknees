from serialize import Serializer
from scraped import IndividualScraped, ScrapedIndex

HIKE_FILE_PATH = "out/hikes.tsv"

print("Scraping index page for hikes...")

hikes = []
next_jump = "https://www.wta.org/go-outside/hikes"

while next_jump:
    list_of_hikes, next_jump = ScrapedIndex().all_hikes(next_jump)
    print ("Nagivating to next page.", next_jump)
    for link in list_of_hikes:
        hike = IndividualScraped(link).hike
        hikes.append(hike)


print(f"Writing hikes to file: '{HIKE_FILE_PATH}'")
Serializer(HIKE_FILE_PATH).serialize(hikes)
print("Done!")

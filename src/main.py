from serialize import Serializer
from scraped import IndividualScraped, ScrapedIndex

HIKE_FILE_PATH = "out/hikes.tsv"

print("Scraping index page for hikes...")

hikes = []

for link in ScrapedIndex().all_hikes():
    hike = IndividualScraped(link).hike
    hikes.append(hike)


print(f"Writing hikes to file: '{HIKE_FILE_PATH}'")
Serializer(HIKE_FILE_PATH).serialize(hikes)
print("Done!")

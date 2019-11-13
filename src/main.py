from serialize import Serializer
from scraped import IndividualScraped

HIKE_FILE_PATH = "out/hikes.tsv"

print("Scraping index page for hikes...")

hike = IndividualScraped("https://www.wta.org/go-hiking/hikes/thorp-mountain-lookout-via-thorp-creek").hike
hikes = []
hikes.append(hike)
hike = IndividualScraped("https://www.wta.org/go-hiking/hikes/mirror-lake-1").hike
hikes.append(hike)


print(f"Writing hikes to file: '{HIKE_FILE_PATH}'")
Serializer(HIKE_FILE_PATH).serialize(hikes)
print("Done!")

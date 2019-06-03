import pickle
import csv

class Serializer:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_headings(self):
        return ["Name", "Latitude", "Longitude", "Elevation", "Length", "Properties", "Permits", "Pets Allowed"]

    def hike_to_row(self, hike):
        return [hike.name,
                hike.lat,
                hike.long,
                hike.elevation,
                hike.length,
                ",".join(hike.properties),
                ",".join(hike.permits),
                hike.pets_allowed]

    def serialize(self, hikes):
        with open(self.file_path, "w+") as tsv:
            tsv_writer = csv.writer(tsv, delimiter="\t")
            tsv_writer.writerow(self.get_headings())
            for hike in hikes:
                tsv_writer.writerow(self.hike_to_row(hike))

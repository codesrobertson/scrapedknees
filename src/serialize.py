import os
import csv
from hike import Hike

class Serializer:
    NAME = "Name"
    LATITUDE = "Latitude"
    LONGITUDE = "Longitude"
    ELEVATION = "Elevation"
    LENGTH = "Length"
    PROPERTIES = "Properties"
    PERMITS = "Permits"

    def __init__(self, file_path):
        self.file_path = file_path

    def get_headings(self):
        return [self.NAME,
                self.LATITUDE,
                self.LONGITUDE,
                self.ELEVATION,
                self.LENGTH,
                self.PROPERTIES,
                self.PERMITS]

    def hike_to_row(self, hike):
        return [hike.name,
                hike.lat,
                hike.long,
                hike.elevation,
                hike.length,
                ",".join(hike.properties),
                ",".join(hike.permits)]

    def serialize(self, hikes):
        dir = os.path.dirname(self.file_path)
        if dir and not os.path.exists(dir):
            os.makedirs(dir)
        with open(self.file_path, "w+") as tsv:
            tsv_writer = csv.writer(tsv, delimiter="\t")
            tsv_writer.writerow(self.get_headings())
            for hike in hikes:
                tsv_writer.writerow(self.hike_to_row(hike))

    def row_to_hike(self, row):
        return Hike(
            row[self.NAME],
            float(row[self.LATITUDE]),
            float(row[self.LONGITUDE]),
            float(row[self.ELEVATION]),
            float(row[self.LENGTH]),
            row[self.PROPERTIES].split(","),
            row[self.PERMITS].split(","))

    def deserialize(self):
        hikes = []
        with open(self.file_path) as tsv:
            tsv_reader = csv.DictReader(tsv, dialect="excel-tab")
            for row in tsv_reader:
                hikes.append(self.row_to_hike(row))
        return hikes

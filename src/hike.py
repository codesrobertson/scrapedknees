class Hike:
    """
    Stores data for a hiking trail

    Attributes:
        name (string): name of the hike
        lat (number): latitude
        long (number): longitude
        elevation (number): highest point in hike
        length (number): hike distance in miles
        properties (list of strings): the features of the hike, e.g. ["waterfall", "forest"]
        permits (list of strings): the types of permits allowed for parking e.g. ["discover", "icon"]
        pets_allowed (boolean): whether pets are allowed on the hike
    """
    def __init__(self, name, lat, long, elevation, length, properties, permits, pets_allowed):
        self.name = name
        self.lat = lat
        self.long = long
        self.elevation = elevation
        self.length = length
        self.properties = properties
        self.permits = permits
        self.pets_allowed = pets_allowed

    def __str__(self):
        return "Hike[" + self.name + ", coordinates:(" + str(self.lat) + ", " + str(self.long) + "), " \
               + "elevation:" + str(self.elevation) + ", length:" + str(self.length ) + " miles, " \
               + "properties:" + str(self.properties) + ", permits:" + str(self.permits)\
               + ", pets are allowed:" + str(self.pets_allowed) + "]"

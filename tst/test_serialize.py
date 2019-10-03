from hike import Hike
from serialize import Serializer

def test_serialize_hike():
    hike = Hike("Nice Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"], True)
    tsv = Serializer("test_hikes.tsv")
    tsv.serialize([hike])

def test_serialize_multiple_hikes():
    hikes = [
        Hike("Nice Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"], True),
        Hike("Cool Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"], True),
        Hike("Chill Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"], True),
        Hike("Decent Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"], True)
    ]
    tsv = Serializer("test_hikes_multiple.tsv")
    tsv.serialize(hikes)

test_serialize_hike()
test_serialize_multiple_hikes()

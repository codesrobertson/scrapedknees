from hike import Hike
from serialize import Serializer

SINGLE_HIKE_FILE = "test_hikes.tsv"
MULTI_HIKE_FILE = "test_hikes_multiple.tsv"


def test_serialize_hike():
    hike = Hike("Nice Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"])
    tsv = Serializer(SINGLE_HIKE_FILE)
    tsv.serialize([hike])


def test_serialize_multiple_hikes():
    hikes = [
        Hike("Nice Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"]),
        Hike("Cool Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"]),
        Hike("Chill Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"]),
        Hike("Decent Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"])
    ]
    tsv = Serializer(MULTI_HIKE_FILE)
    tsv.serialize(hikes)


def test_deserialize_hike():
    tsv = Serializer(SINGLE_HIKE_FILE)

    hike = tsv.deserialize()[0]

    assert hike.name == "Nice Trail"
    assert hike.lat == 100.2221
    assert hike.long == 20.00
    assert hike.elevation == 200
    assert hike.length == 5
    assert hike.properties == ["forest", "waterfall"]
    assert hike.permits == ["icon"]


def test_deserialize_multiple_hikes():
    tsv = Serializer(MULTI_HIKE_FILE)

    all_hikes = tsv.deserialize()
    hike_names = ["Nice Trail", "Cool Trail", "Chill Trail", "Decent Trail"]

    for index, hike in enumerate(all_hikes):
        assert hike.name == hike_names[index]
        assert hike.lat == 100.2221
        assert hike.long == 20.00
        assert hike.elevation == 200
        assert hike.length == 5
        assert hike.properties == ["forest", "waterfall"]
        assert hike.permits == ["icon"]


test_serialize_hike()
test_serialize_multiple_hikes()
test_deserialize_hike()
test_deserialize_multiple_hikes()
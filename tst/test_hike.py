from hike import Hike


def test_create_hike():
    hike = Hike("Nice Trail", 100.2221, 20.00, 200, 5, ["forest", "waterfall"], ["icon"], True)
    print(hike)

test_create_hike()

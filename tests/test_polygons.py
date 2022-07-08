def test_poly_with_holes(adapter):
    adapter.simplify("./test/poly_with_hole.shp", 2, "./data/poly_with_holes_2%.shp")

def test_long_poly(adapter):
    adapter.simplify("./test/long_poly.shp", 0.1, "./data/long_poly_0.1%.shp")



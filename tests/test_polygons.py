def test_poly_with_holes(adapter):
    adapter.simplify("./test_data/poly_with_hole.shp", 2, "./results/poly_with_holes_2%.shp")

def test_long_poly(adapter):
    adapter.simplify("./test_data/long_poly.shp", 0.1, "./results/long_poly_0.1%.shp")



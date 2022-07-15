import json

def test_poly_with_holes(adapter):
    percentage = 2
    input="./test_data/poly_with_hole.geojson"
    output="./results/poly_with_holes_2%.geojson"

    adapter.simplify(input,percentage, output)
    assert (count_vertices(output))/(count_vertices(input))*100-2.5 <= percentage \
        and percentage <= (count_vertices(output))/(count_vertices(input))*100


def test_long_poly(adapter):
    percentage = 0.1
    input="./test_data/long_poly.geojson"
    output="./results/long_poly_0.1%.geojson"

    adapter.simplify(input,percentage, output)
    assert (count_vertices(output))/(count_vertices(input))*100-0.1 <= percentage \
        and percentage <= (count_vertices(output)+5)/(count_vertices(input))*100+0.1

def count_vertices(path_to_file):
    with open(path_to_file) as f:
        gj = json.load(f)
    n=0
    for poly in gj['features'][0]['geometry']['coordinates']:
        for part in poly:
            n+=len(part)
    return n


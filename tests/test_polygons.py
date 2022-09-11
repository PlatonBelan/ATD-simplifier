import json
import pytest

@pytest.mark.parametrize('percentage', [1, 2, 10, 50])
def test_poly_with_holes(adapter, percentage):
    input="./test_data/poly_with_hole.geojson"
    output="./results/poly_with_holes_"+str(percentage)+"%.geojson"

    adapter.simplify(input,percentage, output)
    real_percentage=(count_vertices(output))/(count_vertices(input))*100
    assert real_percentage-2.5 <= percentage \
        and percentage <= real_percentage

@pytest.mark.parametrize('percentage', [0.1, 2, 5, 25])
def test_long_poly(adapter, percentage):
    input="./test_data/long_poly.geojson"
    output="./results/long_poly_"+str(percentage)+"%.geojson"

    adapter.simplify(input,percentage, output)
    real_percentage=(count_vertices(output))/(count_vertices(input))*100
    assert real_percentage-0.15 <= percentage \
        and percentage <= real_percentage+0.15

def count_vertices(path_to_file):
    with open(path_to_file) as f:
        gj = json.load(f)
    n=0
    poly_type=gj['features'][0]['geometry']['type']

    if poly_type=='MultiPolygon':
        coord_list=gj['features'][0]['geometry']['coordinates'] # [[[area1], [hole1], [holeN]], [[area2]]]
        for area in coord_list:
            for part in area:
                n+=len(part)
    elif poly_type=='Polygon':
        for feature in gj['features']:
            coord_list=feature['geometry']['coordinates'] # [[area], [hole1], [holeN]]
            for area in coord_list:
                n+=len(area)
    return n


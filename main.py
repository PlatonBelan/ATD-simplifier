from ATDsimplifier.simplifier import Simplifier
from ATDsimplifier import choose_adaper

percentage=10
adapter=choose_adaper(percentage)
simplifier = Simplifier(
    input_file="./test_data/test_data.shp", adapter=adapter)
boundary_simplified = simplifier.simplify(percentage)

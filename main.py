from ATDsimplifier.simplifier import Simplifier
from ATDsimplifier import choose_adaper

percentage = 10
adapter = choose_adaper(percentage)  # choose the most suitable adapter
# for a given percentage of remaining vertices
simplifier = Simplifier(
    input_file="./test_data/test_data.shp", adapter=adapter)
simplifier.simplify(percentage)
# output file (*.shp) will be written to ./results/

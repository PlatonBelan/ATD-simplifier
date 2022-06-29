from ATDsimplifier.adapter_mapshaper_simplifier import Adapter_simplifier2mapshaper
from ATDsimplifier.mapshaper_simplifier import Mapshaper_simplifier

simplifier=Adapter_simplifier2mapshaper(Mapshaper_simplifier(input_file="D:/ATD-simplifier/test/test_data.shp"))
boundary_10=simplifier.simplify(10)
boundary_10=simplifier.simplify(30)

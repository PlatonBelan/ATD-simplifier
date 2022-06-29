import ATDsimplifier

simplifier=ATDsimplifier.simplifier.Simplifier(input_file="D:/ATD-simplifier/test/test_data.shp")
boundary_10=simplifier.simplify(10)
boundary_10=simplifier.simplify(30)

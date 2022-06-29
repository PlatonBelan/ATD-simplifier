#!/usr/bin/env python
from ATDsimplifier.simplifier import Simplifier


if __name__=="__main__":
    simplifier=Simplifier(input_file="D:/ATD-simplifier/test/test_data.shp")
    boundary_10=simplifier.simplify(10)
    boundary_10=simplifier.simplify(30)
    RUN_FROM_CONSOLE=True

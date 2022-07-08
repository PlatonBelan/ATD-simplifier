#!/usr/bin/env python


if __name__=="__main__":
    simplifier=Simplifier(input_file="D:/ATD-simplifier/test_data/test_data.shp")
    boundary_10=simplifier.simplify(10)
    boundary_10=simplifier.simplify(30)

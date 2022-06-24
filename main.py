from simplifier import Simplifier


if __name__=="__main__":
    simplifier=Simplifier(input_file="./test/boundary-polygon-lvl6.shp")
    boundary_10=simplifier.simplify(10)
    boundary_10=simplifier.simplify(30)

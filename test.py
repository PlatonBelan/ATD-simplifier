import subprocess as sp
sp.run(["node", "./node_modules/mapshaper/mapshaper.js"])

infile="./test/boundary-polygon-lvl6.shp"
#percentage=int(input("Enter percentage of vertices to keep: "))
#format=input("Specify output format (shapefile|geojson|topojson|json|dbf|csv|tsv|svg): ") #shapefile
#outfile=input("Specify the path to output file")#./data/out.shp



sp.run(["mapshaper", infile, "-simplify",
          "weighted", "10%", "-o", "format=shapefile", "./data/out10.shp"])
sp.run(["mapshaper", infile, "-simplify",
          "weighted", "25%", "-o", "format=shapefile", "./data/out25"])
sp.run(["mapshaper", infile, "-simplify",
          "weighted", "50%", "-o", "format=shapefile", "./data/out50"])
sp.run(["mapshaper", infile, "-simplify",
          "weighted", "75%", "-o", "format=shapefile", "./data/out75"])


import os

os.system("d:")
os.system("cd ATD-simplifier")

os.system("node ./node_modules/mapshaper/mapshaper.js")
os.system("mapshaper ./test/boundary-polygon-lvl6.shp - simplify\
          weighted 10% -o format=shapefile ./data/out10.shp")
os.system("mapshaper ./test/boundary-polygon-lvl6.shp - simplify\
          weighted 25% -o format=shapefile ./data/out25.shp")
os.system("mapshaper ./test/boundary-polygon-lvl6.shp - simplify\
          weighted 50% -o format=shapefile ./data/out50.shp")
os.system("mapshaper ./test/boundary-polygon-lvl6.shp - simplify\
          weighted 75% -o format=shapefile ./data/out75.shp")

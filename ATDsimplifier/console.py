from os import system


def mapshaper_command(infile, percentage="10%", output="./data/out10.shp"):
    system("node ../node_modules/mapshaper/mapshaper.js")
    system("mapshaper "+infile+" -simplify weighted "+percentage +
           " -o format=shapefile " + output)

from os import system


def mapshaper_command(infile, percentage="10%", output="./data/out10.shp"):
    system("node ./node_modules/mapshaper/mapshaper.js")
    print(infile)
    print(percentage)
    print(output)
    system("mapshaper "+infile+" -simplify weighted "+percentage +
           " -o format=shapefile " + output)

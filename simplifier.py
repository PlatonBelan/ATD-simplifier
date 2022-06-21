from subprocess import run
from sys import argv


def mapshaper_command():
    run(["node", "./node_modules/mapshaper/mapshaper.js"])
    infile, percentage = argv[1], argv[2]
    run(["mapshaper", infile, "-simplify", "weighted",
         percentage, "-o", "format=shapefile", "./data/result.shp"])


mapshaper_command()

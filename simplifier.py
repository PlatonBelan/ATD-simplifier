import os.path
from subprocess import run


class Simplifier:

    def __init__(self,
                 input_file,
                 percentage):
        self.input_path = os.path.abspath(input_file)
        self.percentage = percentage
        self.simplify()

    def simplify(self):
        run(["node", "./node_modules/mapshaper/mapshaper.js"])
        run(["mapshaper",  self.input_path, "-simplify", "weighted",
            self.percentage, "-o", "format=shapefile", "./data/result.shp"])

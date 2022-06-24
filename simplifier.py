import os.path
from subprocess import run


class Simplifier:

    def __init__(self,
                 input_file):
        self.input_path = input_file

    def simplify(self, percentage):
        run(["node", "./node_modules/mapshaper/mapshaper.js"])
        if type(percentage)==int:
            percentage=str(percentage)+'%'
        output="./data/result_"+percentage+".shp"
        run(["mapshaper",  self.input_path, "-simplify", "weighted",
            percentage, "-o", "format=shapefile", output])

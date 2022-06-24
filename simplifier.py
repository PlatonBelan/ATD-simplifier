import subprocess as sp
from distutils.version import StrictVersion
from sys import stderr


class Simplifier:

    def __init__(self,
                 input_file):
        self.input_path = input_file
        self.check_node()

    def check_node(self):
        checking = sp.Popen(["node", "-v"], stdout=sp.PIPE, stderr=sp.STDOUT, encoding='UTF-8')
        version, errs = checking.communicate()
        if StrictVersion(version[1:]) >= StrictVersion("12.0.0"):
            print("Node version is actual")
        else:
            print('Please, update node')
        if errs:
            print('Please, install node')

    def simplify(self, percentage):
        sp.Popen(["node", "./node_modules/mapshaper/mapshaper.js"])
        if type(percentage) == int:
            percentage = str(percentage)+'%'
        output = "./data/result_"+percentage+".shp"
        sp.Popen(["mapshaper",  self.input_path, "-simplify", "weighted",
               percentage, "-o", "format=shapefile", output])

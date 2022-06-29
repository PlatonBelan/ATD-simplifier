import subprocess as sp
from distutils.version import StrictVersion
from logger import log
from console import mapshaper_command
from os import path


class Simplifier:

    def __init__(self,
                 input_file):
        self.input_path = input_file
        self.check_node()

    def check_node(self):
        checking = sp.Popen(["node", "-v"], stdout=sp.PIPE,
                            stderr=sp.STDOUT, encoding='UTF-8')
        version, errs = checking.communicate()
        if StrictVersion(version[1:]) >= StrictVersion("12.0.0"):
            log.debug("Node version is actual")
        else:
            log.debug('Please, update node')
        if errs:
            log.debug('Please, install node')

    def simplify(self, percentage):
        if type(percentage) == int:
            percentage = str(percentage)+'%'
        log.debug("Start simplify "+self.input_path)
        output = "./data/result_"+percentage+".shp"
        mapshaper_command(infile=self.input_path, percentage=percentage, output=output)
        log.debug("Simplification is finished. " +
                  percentage + " vertices left")
        log.debug("Output file: "+ path.abspath(output))

from os import system
from os import path
import subprocess as sp
from ATDsimplifier.interface import ISimplifier
from distutils.version import StrictVersion
from ATDsimplifier.logger import log


class Mapshaper_simplifier(ISimplifier):
    def __init__(self, input_file):
        self.input_path = self.get_path(input_file)
        self.check_node()

    def get_path(self, input_file):
        return path.abspath(input_file)

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

    def simplify(self, percentage, output):
        system("node ./node_modules/mapshaper/mapshaper.js")
        system("mapshaper "+self.input_path+" -simplify weighted "+percentage +
               " -o format=shapefile " + output)

from ATDsimplifier.interface import ISimplifier
from ATDsimplifier.logger import log
from os import system
from os import path
import subprocess as sp
from distutils.version import StrictVersion
from pathlib import PurePath


class AdapterMapshaper2Simplifier(ISimplifier):
    def check(self):
        checking = sp.Popen(["node", "-v"], stdout=sp.PIPE,
                            stderr=sp.STDOUT, encoding='UTF-8')
        version, errs = checking.communicate()
        if StrictVersion(version[1:]) >= StrictVersion("12.0.0"):
            log.debug("Node version is actual")
        else:
            log.debug('Please, update node')
        if errs:
            log.debug('Please, install node')

    def get_path(self):
        pass

    def simplify(self, input_path, percentage: float, output):
        percentage = str(percentage)+'%'
        if path.isfile(input_path):
            if PurePath(output).match("*.shp"):
                system("node ./node_modules/mapshaper/mapshaper.js")
                system("mapshaper "+input_path+" -simplify weighted "+percentage +
                    " -o format=shapefile " + output)
            elif PurePath(output).match("*.geojson"):
                system("node ./node_modules/mapshaper/mapshaper.js")
                system("mapshaper "+input_path+" -simplify weighted "+percentage +
                    " -o format=geojson " + output)
            else:
                raise ValueError
        else:
            raise FileNotFoundError


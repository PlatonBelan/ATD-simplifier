from ATDsimplifier.interface import ISimplifier
from ATDsimplifier.mapshaper_simplifier import Mapshaper_simplifier
from ATDsimplifier.logger import log


class Adapter_simplifier2mapshaper(ISimplifier):
    def __init__(self,
                 simplifier: Mapshaper_simplifier):
        self.simplifier = simplifier
        self.input_path = self.get_path()

    def get_path(self):
        return self.simplifier.input_path

    def simplify(self, percentage):
        if type(percentage) == int:
            percentage = str(percentage)+'%'
        log.debug("Start simplify "+self.input_path)
        output = "./data/result_"+percentage+".shp"

        self.simplifier.simplify(percentage=percentage, output=output)
        log.debug("Simplification is finished. " +
                  percentage + " vertices left")
        log.debug("Output file: " + self.input_path)

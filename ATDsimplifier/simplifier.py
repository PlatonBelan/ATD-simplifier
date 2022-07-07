from os import path
from ATDsimplifier.logger import log
from ATDsimplifier.interface import ISimplifier
from adapters.adapter_mapshaper_simplifier import AdapterMapshaper2Simplifier


class Simplifier(ISimplifier):

    def __init__(self, input_file, adapter: ISimplifier):
        self.adapter = adapter
        self.input_path = self.get_path(input_file)
        self.check()

    def get_path(self, input_file):
        return path.relpath(input_file, start="../adapters")

    def check(self):
        self.adapter.check()

    def simplify(self, percentage: float):
        if 0.0 > percentage and percentage > 100.0:
            raise ValueError
        try:
            log.debug("Start simplify "+self.input_path)
            output = "./data/result_"+str(percentage)+"%.shp"

            self.adapter.simplify(self.input_path, percentage, output)

            log.debug("Simplification is finished. " +
                      percentage + " vertices left")
            log.debug("Output file: " + self.input_path)
        except Exception:
            log.error("Error: There are problems with the adapter or parameters.\
                \nCheck the data types or contact the developer")

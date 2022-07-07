from sympy import im
from ATDsimplifier.simplifier import Simplifier
from adapters.adapter_mapshaper_simplifier import AdapterMapshaper2Simplifier
from configparser import ConfigParser

config=ConfigParser()
config.read('config.ini')

adapter=AdapterMapshaper2Simplifier()
simplifier=Simplifier(input_file=str(config['simplifier']['input']), adapter=adapter)
boundary_simplified=simplifier.simplify(float(config['simplifier']['percentage']))

from adapters.adapterMapshaper.adapter_mapshaper_simplifier import AdapterMapshaper2Simplifier
from configparser import ConfigParser

config=ConfigParser()
config.read('config.ini')

if str(config['simplifier']['adapter']) == 'AdapterMapshaper':
    alias=str(config['simplifier']['adapter'])
    dict_adapter_alias={alias: AdapterMapshaper2Simplifier}

def choose_adaper(percentage):
    if 0 <= percentage and percentage <= float(config['simplifier']['percentage']):
        return dict_adapter_alias[alias]()

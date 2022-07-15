from ATDsimplifier.simplifier import Simplifier
from adapters.adapterMapshaper.adapter_mapshaper_simplifier import AdapterMapshaper2Simplifier

import pytest


@pytest.fixture(scope="module")
def simplifier():
    return Simplifier("./test_data/test_data.shp", AdapterMapshaper2Simplifier())


@pytest.fixture(scope="module")
def adapter():
    return AdapterMapshaper2Simplifier()

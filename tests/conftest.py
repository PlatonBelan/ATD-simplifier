from ATDsimplifier.simplifier import Simplifier
from adapters.adapter_mapshaper_simplifier import AdapterMapshaper2Simplifier

import pytest

@pytest.fixture(scope="module")
def simplifier():
    return Simplifier("./test/test_data.shp", AdapterMapshaper2Simplifier())

import pytest
from os import path


def test_input_file_exist(simplifier):
    assert path.isfile(simplifier.input_path), 'file not exist'

@pytest.mark.parametrize('percentage', [10, 21.3, 100])
def test_percentage_good(simplifier, percentage):
    simplifier.simplify(percentage)

@pytest.mark.parametrize('percentage', [-1, -100, 152])
def test_percentage_outrange(simplifier, percentage):
    try:
        simplifier.simplify(percentage)
    except ValueError:
        print ('percentage out of range')

@pytest.mark.parametrize('percentage', ['10', '28%', '158%', 'abc', 'five', (10,20)])
def test_percentage_wrong_type(simplifier, percentage):
    try:
        simplifier.simplify(percentage)
    except TypeError:
        print ('percentage must be number')


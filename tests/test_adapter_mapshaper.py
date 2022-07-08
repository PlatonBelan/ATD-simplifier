import pytest


def test_adapter_good(adapter):
    adapter.simplify("./test_data/test_data.shp", 10, "./results/result_10%.shp")


def test_input_path_wrong(adapter):
    try:
        adapter.simplify("wrong_file.shp", 10, "./results/result_10%.shp")
    except FileNotFoundError:
        print('File not found or not exist')


@pytest.mark.parametrize('percentage', [10, 21.3, 100])
def test_percentage_good(adapter, percentage):
    adapter.simplify("./test_data/test_data.shp", percentage,
                     "./results/result_10%.shp")

@pytest.mark.parametrize('percentage', ['10', '28%', '158%', 'abc', 'five', (10, 20)])
def test_percentage_wrong_type(adapter, percentage):
    try:
        adapter.simplify("./test_data/test_data.shp", percentage,
                         "./results/result_10%.shp")
    except TypeError:
        print('percentage must be number')


def test_input_path_wrong(adapter):
    try:
        adapter.simplify("./test_data/test_data.shp", 10, "./results/result_10%.shp")
    except FileNotFoundError:
        print('File not found or not exist')


def test_output_format_wrong(adapter):
    try:
        adapter.simplify("./test_data/test_data.shp", 10, "./results/result_10%.shape")
    except ValueError:
        print("output in wrong format")

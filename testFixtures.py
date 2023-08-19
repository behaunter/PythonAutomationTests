import pytest

@pytest.fixture(scope='function')
def data_list_fixture():
    data = [1, 2, 3, 4, 5]
    return data

@pytest.fixture
def data_dict_fixture():
    data = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    print("Фикстура : начало")
    yield data
    print("Фикстура: конец")


def test_data_list_fixture(data_list_fixture):
    assert len(data_list_fixture) == 5
    assert sum(data_list_fixture) == 15

def test_data_fixtures( data_dict_fixture):
    assert 'key1' in data_dict_fixture


def test_data_dict_fixture(data_dict_fixture):
    assert len(data_dict_fixture) == 3
    assert 'key3' in data_dict_fixture


def test_data_list_more_than_0(data_list_fixture):
    assert sum(data_list_fixture) > 0


def test_data_dict_more_than_0(data_dict_fixture):
    assert len(data_dict_fixture) > 0

if __name__ == "__main__":
    pytest.main()
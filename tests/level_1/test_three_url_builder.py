import pytest

from functions.level_1.three_url_builder import build_url


def test_build_url():
    host_name = 'my-host-name'
    relative_url = 'user/register'
    get_params = {'key1': 'value1', 'key2': 'value2'}
    assert build_url(host_name, relative_url, get_params) == 'my-host-name/user/register?key1=value1&key2=value2'


@pytest.mark.parametrize('host_name, relative_url, get_params, exception',
                         [
                             ('my-host-name', 'user/register', [1, 2, 3], AttributeError),
                             ('my-host-name', 'user/register', set('1234'), AttributeError),
                         ])
def test_exceptions_build_url(host_name, relative_url, get_params, exception):
    with pytest.raises(exception):
        build_url(host_name, relative_url, get_params)

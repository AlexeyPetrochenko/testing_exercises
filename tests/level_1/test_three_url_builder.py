import pytest

from functions.level_1.three_url_builder import build_url


def test__build_url__successful_case_with_parameters():
    host_name = 'my-host-name'
    relative_url = 'user/register'
    get_params = {'key1': 'value1', 'key2': 'value2'}
    
    result = build_url(host_name, relative_url, get_params)
    
    assert result == 'my-host-name/user/register?key1=value1&key2=value2'
    
    
def test__build_url__successful_case_with_one_parameter():
    host_name = 'my-host-name'
    relative_url = 'user/register'
    get_params = {'key1': 'value1'}
    
    result = build_url(host_name, relative_url, get_params)
    
    assert result == 'my-host-name/user/register?key1=value1'
    
    
def test__build_url__successful_case_no_parameters():
    host_name = 'my-host-name'
    relative_url = 'user/register'
    
    result = build_url(host_name, relative_url)
    
    assert result == 'my-host-name/user/register'


def test__build_url__successful_case_empty_parameters():
    host_name = 'my-host-name'
    relative_url = 'user/register'
    params = {}
    
    result = build_url(host_name, relative_url, params)
    
    assert result == 'my-host-name/user/register'


@pytest.mark.parametrize('host_name, relative_url, answer',
                         [
                             ('', '', '/'),
                             ('my-host-name', '', 'my-host-name/'),
                             ('', 'user/register', '/user/register'),
                         ])
def test__build_url__corner_cases(host_name, relative_url, answer):
    assert build_url(host_name, relative_url) == answer


def test__build_url__same_parameters():
    host_name = 'my-host-name'
    relative_url = 'user/register'
    params = {'param': 'value1', 'param': 'value2'}
    
    result = build_url(host_name, relative_url, params)
    
    assert result == 'my-host-name/user/register?param=value2'

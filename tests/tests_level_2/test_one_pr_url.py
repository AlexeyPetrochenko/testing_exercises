import pytest
from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__return_true_when_url_is_github_pull_request():
    assert is_github_pull_request_url('https://github.com/AlexeyPetrochenko/testing_exercises/pull/2')
    

@pytest.mark.parametrize('invalid_url', 
                         [
                            'https://github.com/',
                            'https://github.ru/AlexeyPetrochenko/testing_exercises/pull/2',
                            'https://github.com/AlexeyPetrochenko/testing_exercises/push/2',
                            'https://github.com/AlexeyPetrochenko/testing_exercises',
                            'https://www.youtube.com/?app=desktop&hl=ru',
                         ])
def test__is_github_pull_request_url__return_false_for_invalid_format_urls(invalid_url):
    assert is_github_pull_request_url(invalid_url) is False




@pytest.mark.parametrize('any_string', 
                         [
                             '   ',
                             '1234',
                             'hello world'
                         ])
def test__is_github_pull_request_url__return_false_for_any_string_that_is_not_url(any_string):
    assert is_github_pull_request_url(any_string) is False



def test__is_github_pull_request_url__return_false_for_empty_string():
    assert is_github_pull_request_url('') is False
    

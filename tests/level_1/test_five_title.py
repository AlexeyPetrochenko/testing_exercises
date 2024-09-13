import pytest

from functions.level_1.five_title import change_copy_item


def test_title_longer_maximum():
    assert change_copy_item('Текст для тестирования функции', 10) == 'Текст для тестирования функции'

def test_title_short_not_additional_text():
    assert change_copy_item('Текст для тестирования функции') == 'Copy of Текст для тестирования функции'


@pytest.mark.parametrize('title, max_main_item_title_length, answer',
                         [
                             ('Copy of Текст', 100, 'Copy of Текст (2)'),
                             ('Copy of Текст (3)', 100, 'Copy of Текст (4)'),
                             ('Copy of Текст (10000)', 100, 'Copy of Текст (10001)'),
                             ('Copy of Текст (-1)', 100, 'Copy of Текст (-1) (2)'),
                             ('Copy of Текст (0)', 100, 'Copy of Текст (1)'),
                             ('Copy of Текст ()', 100, 'Copy of Текст () (2)'),
                             ('', 100, 'Copy of '),
                         ])
def test_short_title(title, max_main_item_title_length, answer):
    assert change_copy_item(title, max_main_item_title_length) == answer

@pytest.mark.parametrize('title, max_main_item_title_length, exception',
                         [
                             ('Copy of Текст', [100], TypeError),
                             ('Copy of Текст (3)', iter([1, 2, 3]), TypeError),
                             (11, 100, AttributeError),
                         ])
def test_exceptions_change_copy_item(title, max_main_item_title_length, exception):
    with pytest.raises(exception):
        change_copy_item(title, max_main_item_title_length)

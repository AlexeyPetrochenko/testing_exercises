import pytest

from functions.level_1.five_title import change_copy_item


def test__change_copy_item__return_original_title():
    assert change_copy_item('Текст для тестирования функции', 10) == 'Текст для тестирования функции'


def test__change_copy_item__return_title_with_additional_copy_text():
    assert change_copy_item('Текст для тестирования функции') == 'Copy of Текст для тестирования функции'


@pytest.mark.parametrize('title', ['Copy of Текст', 'Copy of Текст ()', 'Copy of'])                            
def test__change_copy_item__adds_copy_number_when_title_begins_copy_text_and_not_have_element_in_brackets(title):
    answer = title + ' ' + '(2)'
    
    result = change_copy_item(title)
    
    assert result == answer


@pytest.mark.parametrize('element_in_brackets', [0, 3, 1000])
def test__change_copy_item__adds_copy_number_when_title_begins_copy_text_and_has_element_in_brackets(element_in_brackets):
    answer = f'Copy of Текст ({element_in_brackets + 1})'
    
    result = change_copy_item(f'Copy of Текст ({element_in_brackets})')
    
    assert result == answer
    
    
def test__change_copy_item__adds_copy_number_when_title_begins_copy_text_and_has_negative_number_in_brackets():
    change_copy_item('Copy of Текст (-1)') == 'Copy of Текст (-1) (2)'

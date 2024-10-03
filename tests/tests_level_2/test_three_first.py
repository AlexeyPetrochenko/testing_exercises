import pytest

from functions.level_2.three_first import first


def test__first__return_first_element_from_items():
    assert first(items=[1, 2, 3, 4, 5]) == 1


def test__first__return_first_element_from_items_when_he_is_alone():
    assert first(items=[5]) == 5
    

def test__first__raise_attribute_error_when_items_is_empty_and_default_not_set():
    with pytest.raises(AttributeError):
        first(items=[])


def test__first__raise_attribute_error_when_items_is_empty_and_default_string_is_equal_to_variable_not_set():
    with pytest.raises(AttributeError):
        first(items=[], default="NOT_SET")

        
@pytest.mark.parametrize('default', [0, None, '', 'default', 100000, 1, -12, '   '])     
def test__first__return_default_when_items_is_empty_and_default_set(default):
    assert first(items=[], default=default) == default
    
@pytest.mark.parametrize('default', [0, None, '', 'default', 100000, 1, -12, '   '])  
def test__first__return_first_element_when_passed_items_and_variable_default(default):
    assert first([1, 2, 3, 5], default) == 1
    
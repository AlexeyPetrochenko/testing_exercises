import pytest
from decimal import Decimal

from functions.level_3.two_expense_categorizer import guess_expense_category, is_string_contains_trigger
from functions.level_3.models import ExpenseCategory


@pytest.mark.parametrize('spent_in, category', [
    ('Bar asador set', ExpenseCategory.BAR_RESTAURANT),
    ('meat house', ExpenseCategory.SUPERMARKET),
    ('pharm, near home', ExpenseCategory.MEDICINE_PHARMACY),
    (' yandex go', ExpenseCategory.TRANSPORT),
    
])
def test__guess_expense_category__successful_category_definition(spent_in, category, create_expense):
    assert guess_expense_category(create_expense(spent_in=spent_in)) == category
       

@pytest.mark.parametrize('spent_in', [
    'does not contain trigger words',
    '',
    '     ',
    '1234'
])
def test__guess_expense_category__does_not_contain_trigger_words(spent_in, create_expense):
    assert guess_expense_category(create_expense(spent_in=spent_in)) is None


def test__string_contains_trigger__original_string_matches_trigger():
    assert is_string_contains_trigger(original_string='hello', trigger='hello') is True
    
@pytest.mark.parametrize('original_string', ['hello', 'hello,', 'hello.', 'hello-'])
def test__string_contains_trigger__original_string_starts_with_trigger(original_string):
    assert is_string_contains_trigger(original_string='hello', trigger='hello') is True


@pytest.mark.parametrize('original_string', [',hello', '.hello', '-hello'])
def test__string_contains_trigger__original_string_ends_with_trigger(original_string):
    assert is_string_contains_trigger(original_string='hello', trigger='hello') is True
    
    
@pytest.mark.parametrize('original_string', [',hello.', '.hello-', '-hello,'])
def test__string_contains_trigger__original_string_contains_trigger(original_string):
    assert is_string_contains_trigger(original_string='hello', trigger='hello') is True
    

def test__guess_expense_category__original_string_register_independent():
    assert is_string_contains_trigger(original_string='HELLO', trigger='hello') is True


def test__guess_expense_category__always_false_if_trigger_is_capitalized():
    assert is_string_contains_trigger(original_string='HELLO', trigger='HELLO') is False



from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
from functions.level_3.models import Currency
import datetime
from decimal import Decimal
import pytest
from statistics import StatisticsError


def test__calculate_average_daily_expenses__when_one_expense_entry(create_expense):
    assert calculate_average_daily_expenses([create_expense(amount=Decimal(10))]) == Decimal(10)
    

def test__calculate_average_daily_expenses__exception_when_no_expenses():
    with pytest.raises(StatisticsError):
        expenses = []
        calculate_average_daily_expenses(expenses)
        

def test__calculate_average_daily_expenses__average_expenses_on_different_days(create_expense):
    date_today = datetime.datetime.now()
    date_yesterday = date_today - datetime.timedelta(days=1)
    expenses_today = [create_expense(amount=amount, spent_at=date_today) for amount in range(1, 5)]
    expenses_yesterday = [create_expense(amount=amount, spent_at=date_yesterday) for amount in range(1, 4)]
    
    result = calculate_average_daily_expenses(expenses_today + expenses_yesterday)
    
    assert result == Decimal(8)
    

def test__calculate_average_daily_expenses__when_all_expenses_in_one_day(create_expense):
    date_today = datetime.datetime.now()
    expenses = [create_expense(amount=amount, spent_at=date_today) for amount in range(1, 5)]

    result = calculate_average_daily_expenses(expenses)
    
    assert result == Decimal(10)

        
def test__calculate_average_daily_expenses__when_expenses_different_currencies(create_expense):
    expenses_in_rub = create_expense(currency=Currency.RUB)
    expenses_in_usd = create_expense(currency=Currency.USD)
    
    result = calculate_average_daily_expenses([expenses_in_rub, expenses_in_usd])
    
    assert result == Decimal(20)
    

def test__calculate_average_daily_expenses__when_transactions_from_different_cards(create_bank_card, create_expense):
    first_card = create_bank_card('1111', 'Owner')
    second_card = create_bank_card('0000', 'Owner')
    
    expenses_first_card = [create_expense(card=first_card, amount=amount) for amount in range(1, 5)]
    expenses_second_card = [create_expense(card=second_card, amount=amount) for amount in range(1, 5)]
    
    result = calculate_average_daily_expenses(expenses_first_card + expenses_second_card)
    
    assert result == Decimal(20)

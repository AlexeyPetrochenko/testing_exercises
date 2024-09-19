from decimal import Decimal
import decimal
import pytest
import datetime
from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


@pytest.fixture()
def get_sms():
    sms = SmsMessage(
        text='1000.99 р, 2200700104218943 24.01.24 16:45 Магнит-Косметик ул.Фрунзе д.25 authcode ',
        author='Tinkoff Bank', 
        sent_at=datetime.datetime.now()
    )
    return sms


def test__parse_ineco_expense__parses_expenses_correctly(get_sms):
    bank_card_first = BankCard(last_digits='8943', owner='Alex P')
    bank_card_second = BankCard(last_digits='8921', owner='Alex P')
    
    result = parse_ineco_expense(get_sms, [bank_card_first, bank_card_second])
    
    assert result.amount == Decimal('1000.99')
    

def test__parse_ineco_expense__correctly_parsed_spent_in(get_sms):
    bank_card_first = BankCard(last_digits='8943', owner='Alex P')
    bank_card_second = BankCard(last_digits='8921', owner='Alex P')
    
    result = parse_ineco_expense(get_sms, [bank_card_first, bank_card_second])
    
    assert result.spent_in == 'Магнит-Косметик ул.Фрунзе д.25'
    

def test__parse_ineco_expense__finds_the_right_card(get_sms):
    bank_card_first = BankCard(last_digits='8943', owner='Alex P')
    bank_card_second = BankCard(last_digits='8921', owner='Alex P')
    
    result = parse_ineco_expense(get_sms, [bank_card_first, bank_card_second])
    
    assert result.card.last_digits == bank_card_first.last_digits


def test__parse_ineco_expense__datetime_parsed_successfully(get_sms):
    bank_card_first = BankCard(last_digits='8943', owner='Alex P')
    bank_card_second = BankCard(last_digits='8921', owner='Alex P')
    
    result = parse_ineco_expense(get_sms, [bank_card_first, bank_card_second])
    
    assert result.spent_at == datetime.datetime(day=24, month=1, year=2024, hour=16, minute=45)


@pytest.mark.parametrize('date_of_purchase',
                         [
                             ('24.01.24 16.45'),
                             ('24-01-24 16:45'),
                             ('24.01.24 16.60'),
                             ('24.01.24 24.45'),
                         ])
def test__parse_ineco_expense__exception_on_invalid_date_format(date_of_purchase):
    sms = SmsMessage(
        text=f'1000.99 р, 2200700104218943 {date_of_purchase} Магнит-Косметик ул.Фрунзе д.25 authcode ',
        author='Tinkoff Bank', 
        sent_at=datetime.datetime.now()
    )
    bank_card_first = BankCard(last_digits='8943', owner='Alex P')
    bank_card_second = BankCard(last_digits='8921', owner='Alex P')
    
    with pytest.raises(ValueError):
        parse_ineco_expense(sms, [bank_card_first, bank_card_second])
        

@pytest.mark.parametrize('expense',
                         [
                             ('100,00'),
                         ])
def test__parse_ineco_expense__invalid_expense_format(expense):
    sms = SmsMessage(
        text=f'{expense} р, 2200700104218943 24.01.24 16:45 Магнит-Косметик ул.Фрунзе д.25 authcode ',
        author='Tinkoff Bank', 
        sent_at=datetime.datetime.now()
    )
    bank_card_first = BankCard(last_digits='8943', owner='Alex P')
    bank_card_second = BankCard(last_digits='8921', owner='Alex P')
    
    with pytest.raises(decimal.InvalidOperation):
        parse_ineco_expense(sms, [bank_card_first, bank_card_second])
    
  
def test__parse_ineco_expense__exception_if_no_suitable_card_available(get_sms):
    bank_card2 = BankCard(last_digits='8921', owner='Alex P')
    
    with pytest.raises(IndexError):
        parse_ineco_expense(get_sms, [bank_card2])
        
from decimal import Decimal
import pytest
import datetime



from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


@pytest.fixture()
def correct_sms():
    sms = SmsMessage(text='1000.99 р, 2200700104218943 24.01.24 16:45 Магнит-Косметик ул.Фрунзе д.25 authcode ',
                     author='Tinkoff Bank', sent_at=datetime.datetime.now())
    return sms

@pytest.fixture()
def correct_answer():
    expense = Expense(
        amount=Decimal('1000.99'),
        card=BankCard(last_digits='8943', owner='Alex P'),
        spent_in='Магнит-Косметик ул.Фрунзе д.25',
        spent_at=datetime.datetime(2024, 1, 24, 16, 45))
    return expense


def test_parse_ineco_expense(correct_sms, correct_answer):
    bank_card1 = BankCard(last_digits='8943', owner='Alex P')
    bank_card2 = BankCard(last_digits='8921', owner='Alex P')
    assert parse_ineco_expense(correct_sms, [bank_card2, bank_card1]) == correct_answer

def test_no_suitable_card_available(correct_sms):
    bank_card2 = BankCard(last_digits='8921', owner='Alex P')
    with pytest.raises(IndexError):
        parse_ineco_expense(correct_sms, [bank_card2])
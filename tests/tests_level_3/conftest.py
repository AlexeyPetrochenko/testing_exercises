from pytest import fixture
import decimal
import datetime
from functions.level_3.models import Currency, BankCard, ExpenseCategory, Expense


@fixture
def create_bank_card():
    def create_bank_card_function(last_digits: str = '0000', owner: str = 'Owner'):
        bank_card = BankCard(last_digits=last_digits, owner=owner)
        return bank_card
    return create_bank_card_function


@fixture
def create_expense(create_bank_card):
    def create_expense_function(
        amount: decimal.Decimal = decimal.Decimal(10),
        currency: Currency = Currency.RUB,
        card: BankCard = create_bank_card(),
        spent_in: str = 'Store',
        spent_at: datetime.datetime = datetime.datetime(year=2024, month=1, day=1),
        category: ExpenseCategory | None = None
    ):
        
        expense = Expense(
            amount=amount,
            currency=currency,
            card=card,
            spent_in=spent_in,
            spent_at=spent_at,
            category=category
        ) 
        
        return expense
    return create_expense_function


@fixture
def date_factory():
    def get_date_function(date_str_iso: str = '2024-07-25'):
        return datetime.datetime.strptime(date_str_iso, '%Y-%m-%d')
    return get_date_function

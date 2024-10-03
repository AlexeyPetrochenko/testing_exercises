from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__subscription_check_successful(create_expense, date_factory):
    expense = create_expense(spent_in='Bar')
    expenses_history = [
        create_expense(spent_in='Bar', spent_at=date_factory('2024-01-25')),
        create_expense(spent_in='Bar', spent_at=date_factory('2024-02-25')),
        create_expense(spent_in='Bar', spent_at=date_factory('2024-03-25'))
    ]
    
    result = is_subscription(expense, expenses_history)
    
    assert result is True
    
    
def test__is_subscription__subscription_false_check_subscription_when_more_than_one_expense_per_category_per_month(create_expense, date_factory):
    expense = create_expense(spent_in='Bar')
    expenses_history = [
        create_expense(spent_in='Bar', spent_at=date_factory('2024-01-25')),
        create_expense(spent_in='Bar', spent_at=date_factory('2024-01-25')),
        create_expense(spent_in='Bar', spent_at=date_factory('2024-03-25'))
    ]
    
    result = is_subscription(expense, expenses_history)
    
    assert result is False
    
    
def test__is_subscription__subscription_false_check_subscription_when_less_than_three_same_destination_expenses(create_expense, date_factory):
    expense = create_expense(spent_in='Bar')
    expenses_history = [
        create_expense(spent_in='Bar', spent_at=date_factory('2024-01-25')),
        create_expense(spent_in='Bar', spent_at=date_factory('2024-02-25'))
    ]
    
    result = is_subscription(expense, expenses_history)
    
    assert result is False


def test__is_subscription__subscription_false_check_when_empty_history_expenses(create_expense):
    assert is_subscription(create_expense(), []) is False
    
    
def test__is_subscription__subscription_false_check_when_no_matches_category(create_expense):
    expense = create_expense(spent_in='Bar')
    expenses_history = [
        create_expense(spent_in='food'),
        create_expense(spent_in='beer'),
        create_expense(spent_in='cheeps')
    ]
    
    result = is_subscription(expense, expenses_history)
    
    assert result is False

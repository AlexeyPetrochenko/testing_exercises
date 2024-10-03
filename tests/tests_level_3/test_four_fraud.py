from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__find_fraud_expenses_in_one_chain(create_expense, date_factory):
    history = [
        create_expense(amount=4000, spent_in='Store A', spent_at=date_factory('2024-07-25')),
        create_expense(amount=4000, spent_in='Store A', spent_at=date_factory('2024-07-25')),
        create_expense(amount=4000, spent_in='Store A', spent_at=date_factory('2024-07-25')),
        create_expense(amount=4000, spent_in='Store B', spent_at=date_factory('2024-07-16')),
        create_expense(amount=4000, spent_in='Store B', spent_at=date_factory('2024-07-16')),
    ]
    
    fraud_expenses = find_fraud_expenses(history=history)
    
    assert all([all([e.amount == 4000, e.spent_at == date_factory('2024-07-25'), e.spent_in == 'Store A']) 
                for e in fraud_expenses])
    
    
def test__find_fraud_expenses__no_fraud_expenses_when_amount_more_than_the_max_fraud_amount(create_expense):
    history = [
        create_expense(amount=10000),
        create_expense(amount=10000),
        create_expense(amount=10000),
    ]
    
    result = find_fraud_expenses(history=history)
    
    assert result == []
    
    
def test__find_fraud_expenses__no_fraud_expenses_when_less_min_fraud_chain_length(create_expense, date_factory):
    history = [
        create_expense(amount=4000, spent_in='Store A', spent_at=date_factory('2024-07-25')),
        create_expense(amount=4000, spent_in='Store A', spent_at=date_factory('2024-07-25')),
        create_expense(amount=3000, spent_in='Store B', spent_at=date_factory('2024-07-10')),
        create_expense(amount=3000, spent_in='Store B', spent_at=date_factory('2024-07-10')),
    ]

    result = find_fraud_expenses(history=history)

    assert result == []
    

def test__find_fraud_expenses__find_fraud_expenses_in_several_chain(create_expense, date_factory):
    first_expense = create_expense(amount=4000, spent_in='Store A', spent_at=date_factory('2024-07-25'))
    second_expense = create_expense(amount=2000, spent_in='Store B', spent_at=date_factory('2024-07-10'))
    history = [
        first_expense,
        first_expense,
        first_expense,
        second_expense,
        second_expense,
        second_expense,
    ]
    
    fraud_expenses = find_fraud_expenses(history=history)
    
    assert len(fraud_expenses) == 6 and first_expense in history and second_expense in history

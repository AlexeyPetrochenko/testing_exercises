import pytest
from datetime import datetime, date, time, timedelta

from functions.level_1.two_date_parser import compose_datetime_from


def factory_for_creating_dates_today(date_str: str, time_str: str):
    date_today = date.today()
    time_created = datetime.strptime(time_str, '%H:%M').time()
    created_datetime = datetime.combine(date_today, time_created)
    if date_str == 'tomorrow':
        created_datetime += timedelta(days=1)
    return created_datetime


@pytest.mark.parametrize('time_str',
                         [
                             ('09:15'),
                             ('00:00'),
                             ('00:01'),
                             ('23:59'),
                         ])
def test__compose_datetime_from__date_tomorrow(time_str):
    reference_datetime = factory_for_creating_dates_today('tomorrow', time_str)
    
    result = compose_datetime_from('tomorrow', time_str)
    
    assert result == reference_datetime
    

@pytest.mark.parametrize('date_str', 
                         [
                             ('today'),
                             (''),
                             ('1234'),
                             ('   '),
                             ('any string'),
                         ])
def test__compose_datetime_from__date_today(date_str):
    reference_datetime = factory_for_creating_dates_today(date_str, '15:31')
    
    result = compose_datetime_from(date_str, '15:31')
    
    assert result == reference_datetime
    

@pytest.mark.parametrize('time_str',
                         [
                             ('09:15'),
                             ('15:15'),
                             ('00:00'),
                             ('00:01'),
                             ('23:59'),
                         ])
def test__compose_datetime_from__for_the_correct_time(time_str):
    reference_datetime = factory_for_creating_dates_today('today', time_str)
    
    result = compose_datetime_from('today', time_str)
    
    assert result == reference_datetime
    



@pytest.mark.parametrize('date_str, time_str',
                         [
                             ('today', '24:00'),
                             ('today', '23:60'),
                             ('tomorrow', '23:60'),
                             ('tomorrow', '24:00'),
                         ])
def test__compose_datetime_from__exception_out_of_range_time(date_str, time_str):
    with pytest.raises(ValueError):
        compose_datetime_from(date_str, time_str)


@pytest.mark.parametrize('time_str',
                         [
                             ('13:00:30'),
                             ('23.30'),
                             ('23-23'),
                             ('23'),
                             ('a:10'),
                             (''),
                             ('2347023'),

                         ])
def test__compose_datetime_from__invalid_time_format(time_str):
    with pytest.raises(ValueError):
        compose_datetime_from('today', time_str)

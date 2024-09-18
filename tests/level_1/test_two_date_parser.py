import pytest
from datetime import datetime, date, time, timedelta

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize('date_str, time_str, answer',
                         [
                             ('today', '15:30', datetime.combine(date.today(), time(hour=15, minute=30))),
                             ('today', '00:00', datetime.combine(date.today(), time(hour=0, minute=0))),
                             ('', '23:59', datetime.combine(date.today(), time(hour=23, minute=59))),
                             ('tomorrow', '09:15', datetime.combine(date.today() + timedelta(days=1), time(hour=9, minute=15))),
                         ])
def test_compose_datetime_from(date_str, time_str, answer):
    assert compose_datetime_from(date_str, time_str) == answer


@pytest.mark.parametrize('date_str, time_str',
                         [
                             ('today', '24:00'),
                             ('today', '23:60'),
                             ('today', '-23:15'),
                             ('today', '23:234'),

                         ])
def test_exception_out_of_range_time(date_str, time_str):
    with pytest.raises(ValueError):
        compose_datetime_from(date_str, time_str)


@pytest.mark.parametrize('date_str, time_str',
                         [
                             ('today', '13:00:30'),
                             ('today', '23.30'),
                             ('today', '23-234'),
                             ('today', '23'),
                             ('today', 'a:10'),
                             ('today', ''),

                         ])
def test_exception_unpack(date_str, time_str):
    with pytest.raises(ValueError):
        compose_datetime_from(date_str, time_str)


@pytest.mark.parametrize('date_str, time_str',
                         [
                             ('today', [1,3,4]),
                             ('today', set('adsfge')),
                             ('today', 145),
                         ])
def test_exception_no_attribute(date_str, time_str):
    with pytest.raises(AttributeError):
        compose_datetime_from(date_str, time_str)


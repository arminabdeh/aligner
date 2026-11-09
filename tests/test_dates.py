from datetime import date
from dates import days_between


def test_same_day_is_zero():
    assert days_between(date(2026, 3, 10), date(2026, 3, 10)) == 0


def test_three_days():
    assert days_between(date(2026, 3, 10), date(2026, 3, 13)) == 3

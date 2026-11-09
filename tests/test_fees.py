from datetime import date

from fees import format_fee, late_fee


def test_returned_early_is_free():
    assert late_fee(date(2026, 3, 10), date(2026, 3, 9)) == 0.0


def test_late_return_costs_money():
    assert late_fee(date(2026, 3, 10), date(2026, 3, 14)) > 0


def test_format_fee():
    assert format_fee(1.5) == "$1.50"

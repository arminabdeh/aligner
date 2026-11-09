from datetime import date

from reminders import reminder_for

DUE = date(2026, 3, 10)


def test_due_tomorrow():
    assert reminder_for(date(2026, 3, 9), DUE) == "Your book is due tomorrow."


def test_due_today():
    assert reminder_for(date(2026, 3, 10), DUE) == "Your book is due today."


def test_overdue():
    assert reminder_for(date(2026, 3, 12), DUE) == "Your book is overdue."


def test_no_reminder_a_week_before():
    assert reminder_for(date(2026, 3, 1), DUE) is None

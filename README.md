# tiny-library

A small made-up Python app for practice. It works out late fees for library books and decides which reminder to send.

- dates.py: days_between(start, end)
- fees.py: late_fee(due, returned) and format_fee(amount)
- reminders.py: reminder_for(today, due)

Rule: returning a book on its due date is free, and each day late costs $0.25.

Run the tests from this folder:

    python -m pip install pytest
    python -m pytest -q

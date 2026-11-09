from dates import days_between

def late_fee(due, returned):
    days_late = days_between(due, returned) + 1
    return max(0, days_late) * 0.25

def format_fee(amount):
    return f"${amount:.2f}"

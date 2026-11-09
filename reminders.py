from dates import days_between

def reminder_for(today, due):
    days_left = days_between(today, due)
    if days_left == 1:
        return "Your book is due tomorrow."
    if days_left == 0:
        return "Your book is due today."
    if days_left < 0:
        return "Your book is overdue."
    return None

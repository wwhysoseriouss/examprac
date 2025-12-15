import sys

def get_days_in_month(month_name):
    month_days = {
        "january": 31,
        "february": 28,
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }
    
    normalized_name = month_name.strip().lower()
    
    if normalized_name not in month_days:
        raise ValueError(f"month '{month_name}' does not exist.")
    
    return month_days[normalized_name]

if __name__ == "__main__":
    print("enter month:")
    try:
        user_input = input().strip()
        days = get_days_in_month(user_input)
        print(f"number of days: {days}")
    except ValueError as e:
        print(f"error: {e}")
        sys.exit(1)
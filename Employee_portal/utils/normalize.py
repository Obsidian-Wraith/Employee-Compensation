import re
import pandas as pd
from datetime import datetime
from dateutil import parser

def normalize_yoe(value):
    print(value)
    """
    Normalize 'Years of Experience':
    - "1-2" → 1.5
    - "3+"  → 3.5
    - "" or NaN → 0.0
    - Single digit → float
    """
    if pd.isna(value) or str(value).strip() == '':
        return 0.0

    if isinstance(value, (int, float)):
        return float(value)

    value = str(value).strip()

    match = re.match(r'(\d+)\s*-\s*(\d+)', value)
    if match:
        lo, hi = map(int, match.groups())
        return (lo + hi) / 2

    match = re.match(r'(\d+)\s*\+', value)
    if match:
        return float(match.group(1)) + 0.5

    if value.isdigit():
        return float(value)

    return 0.0


def normalize_active(value):
    """
    Normalize 'Active' field:
    - "Y" / "y" → True
    - "N" / "n" → False
    - Else → False
    """
    if isinstance(value, str) and value.strip().lower() == 'y':
        return True
    return False


def normalize_last_working_day(value):
    """
    Normalize 'Last Working Day':
    - Valid date → formatted 'YYYY-MM-DD' string
    - 'No', NaN, or invalid → ''
    """
    try:
        # Try to parse the input into a datetime object
        dt = parser.parse(str(value), fuzzy=True)
        # Convert to epoch milliseconds
        epoch_milli = int(dt.timestamp() * 1000)
        return str(epoch_milli)
    except (ValueError, OverflowError, TypeError):
        return ''

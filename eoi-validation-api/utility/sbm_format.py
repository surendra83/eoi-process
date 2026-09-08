# core/date_utils.py
from datetime import date, datetime
OUTPUT_DATE_FORMAT = "%m/%d/%Y"

# Formats accepted when the incoming value is a string.
_INPUT_DATE_FORMATS = (
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M:%S.%f",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M:%S.%f",
    "%Y-%m-%d",
    "%m/%d/%Y",
)

def format_date(value, output_format: str = OUTPUT_DATE_FORMAT):
    """Convert a date/datetime/ISO string into MM/DD/YYYY.
    Returns the original value when it cannot be parsed, and None for empty input.
    """
    if value is None or value == "":
        return None

    if isinstance(value, datetime):
        return value.strftime(output_format)

    if isinstance(value, date):
        return value.strftime(output_format)

    if isinstance(value, str):
        text = value.strip()
        for fmt in _INPUT_DATE_FORMATS:
            try:
                return datetime.strptime(text, fmt).strftime(output_format)
            except ValueError:
                continue
        try:
            return datetime.fromisoformat(text.replace("Z", "+00:00")).strftime(output_format)
        except ValueError:
            return value

    return value

def date_formate_in_yyyy_mm_dd(inpdate: str):
    if not inpdate:  # handles None, '', etc.
        return None

    try:
        return datetime.fromisoformat(inpdate).date().isoformat()
    except (ValueError, TypeError):
        return None

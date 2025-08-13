# Days Since & Time Calculator

A utility script that calculates the time elapsed since a specific date, with conversions to days, weeks, months, and years.

## Description

This Python script calculates how much time has passed since a given date. It provides the result in multiple time units (days, weeks, months, years) and includes comprehensive time information display.

## How to Run

```bash
python3 "daysSince&Time.py"
```

Note: Use quotes around the filename due to the special characters.

## Features

- **Date Calculation**: Calculate exact days since any past date
- **Multiple Time Units**: Automatic conversion to weeks, months, and years
- **Date Validation**: Input validation with clear error messages
- **Comprehensive Output**: Displays results in all time units simultaneously
- **Standard Date Format**: Uses ISO format (YYYY-MM-DD) for consistency

## Requirements

- Python 3.x

## Date Format

The script expects dates in **YYYY-MM-DD** format (ISO 8601 standard):
- ✅ Correct: `2020-01-15`
- ❌ Incorrect: `15/01/2020`, `January 15, 2020`

## Example Usage

```
Enter a date (YYYY-MM-DD): 2020-03-15
Days since 2020-03-15: 1215
Weeks since 2020-03-15: 173
Months since 2020-03-15: 40
Years since 2020-03-15: 3

Additional Information:
Days since 2020-03-15: 1215
Weeks since 2020-03-15: 173
Months since 2020-03-15: 40
Years since 2020-03-15: 3
```

```
Enter a date (YYYY-MM-DD): 2024-13-45
Days since 2024-13-45: Invalid date format. Please use YYYY-MM-DD.
```

## Time Conversions

The script uses these conversion ratios:
- **Weeks**: Days ÷ 7
- **Months**: Days ÷ 30 (approximate)
- **Years**: Days ÷ 365 (approximate)

Note: Month and year calculations are approximations and don't account for varying month lengths or leap years.

## Use Cases

- Calculate age in days
- Track project timelines
- Measure time since important events
- Convert between different time units
- Date arithmetic for planning

## How It Works

1. User inputs a date in YYYY-MM-DD format
2. Script parses the date using `datetime.strptime()`
3. Calculates the difference between input date and current date
4. Converts the result to various time units using integer division
5. Displays comprehensive time information

Perfect for date calculations, timeline tracking, and time-based analytics!
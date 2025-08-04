# days since script
import datetime 
def days_since(date_str):
    """Calculate the number of days since a given date."""
    try:
        # Parse the input date string
        input_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        # Get today's date
        today = datetime.datetime.now()
        # Calculate the difference in days
        delta = today - input_date
        return delta.days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

if __name__ == "__main__":
    date_input = input("Enter a date (YYYY-MM-DD): ")
    days = days_since(date_input)
    print(f"Days since {date_input}: {days}")

# to convert to weeks, you can divide the result by 7
    weeks = days // 7
    print(f"Weeks since {date_input}: {weeks}")
    
# to convert to months, you can use a rough estimate of 30 days per month
    months = days // 30
    print(f"Months since {date_input}: {months}")   
    
# to convert to years, you can use a rough estimate of 365 days per year
    years = days // 365
    print(f"Years since {date_input}: {years}")

    print("Additional Information:")
    print(f"Days since {date_input}: {days}")
    print(f"Weeks since {date_input}: {weeks}")
    print(f"Months since {date_input}: {months}")
    print(f"Years since {date_input}: {years}")
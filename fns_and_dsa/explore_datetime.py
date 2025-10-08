from datetime import date, timedelta, datetime
 
def display_current_datetime():
     # Get the current date
     today = datetime.now()
     # Format the current date and time
     formatted_current_datetime = today.strftime("%Y-%m-%d %H:%M:%S")
     return formatted_current_datetime

print(display_current_datetime())
     
def calculate_future_date(days):
    # Get today's date and time
    current_date = datetime.now()
    
    # Add the specified number of days
    future_date = current_date + timedelta(days=days)
    
    # Print the future date in YYYY-MM-DD format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Prompt the user for number of days
try:
    user_input = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(user_input)
except ValueError:
    print("Please enter a valid integer.")



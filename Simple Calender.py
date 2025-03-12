import calendar

# Get user input for the year
year = int(input("Enter the year (e.g., 2025): "))

# Print the calendar for the entire year
print("\nCalendar for the year", year)
print(calendar.TextCalendar(calendar.SUNDAY).formatyear(year))

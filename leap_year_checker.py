# leap_year_checker.py

# Ask the user to enter a year
year = int(input("Enter a year: "))

# Determine if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
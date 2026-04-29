
# Import datetime module
import datetime

# Current date and time
now = datetime.datetime.now()

print("Current Date and Time:", now)


# ====================================
# Current date only
# import datetime

# today = datetime.date.today()

# print("Today Date:", today)
# ==============================


# Current year, month, day
# import datetime

# today = datetime.date.today()

# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)


# ===============================
# import datetime

# now = datetime.datetime.now()

# print("Hour:", now.hour)
# print("Minute:", now.minute)
# print("Second:", now.second)

# Format date and time
# import datetime

# now = datetime.datetime.now()

# print(now.strftime("%d-%m-%Y"))
# print(now.strftime("%I:%M %p"))
# print(now.strftime("%A"))


# ```python
# # Simple age calculator using birth year
# import datetime

# current_year = datetime.date.today().year

# birth_year = int(input("Enter your birth year: "))

# age = current_year - birth_year

# print("Your age is:", age)


# ```text
# datetime → Python ka module hai date/time handle karne ke liye
# now() → current date and time deta hai
# today() → sirf current date deta hai
# strftime() → date/time ko readable format me convert karta hai
# ```

# Prevent crashes from happening and program will contine


# Example
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:           # Similar to the else in "If" function. This will execute if no exceptions occur
    print("No exceptions were thrown")
# If you dont handle exceptions, your program will crash

# Example 2
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:  # You can change the expect clause and specify a different expecption
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")

# OR
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")
finally:  # Executes regardless if exceptions happen or not
    print("Done")

# Example 3 / Raising Exceptions / Try not to use raising method because it causes performance issues /
# Try alternative method to raising exceptions


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age Cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

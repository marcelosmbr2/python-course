# Error Handling 

try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    # Runs only if a ZeroDivisionError occurs
    print("You cannot divide by zero!")
except ValueError:
    # Runs only if a ValueError occurs (e.g., typing text instead of numbers)
    print("Please enter a valid integer.")
else:
    # Runs only if the try block succeeds without any errors
    print(f"Success! The result is {result}")
finally:
    # Always runs, regardless of whether an error occurred or not
    print("Cleaning up resources and closing operations.")
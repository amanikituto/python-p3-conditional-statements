 
def admin_login(username, password):
    """Checks if the provided credentials match the admin login.

    Args:
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        str: "Access granted" if credentials match, "Access denied" otherwise.
    """
    if (username.lower() == "admin") and (password == "12345"):  # .lower() for case-insensitivity
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    """Describes the weather based on temperature.

    Args:
        temperature (int or float): The temperature in Fahrenheit.

    Returns:
        str: A description of the weather.
    """
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(number):
    """Implements the FizzBuzz game.

    Args:
        number (int): The number to check.

    Returns:
        str or int: "Fizz", "Buzz", "FizzBuzz", or the number itself.
    """
    if number % 15 == 0:    # Check divisibility by 15 first (both 3 and 5)
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def calculator(operation, num1, num2):
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            return num1 / num2
        else:
            raise ValueError("Invalid operation!")  # Explicitly raise an error
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None
    
import io
import sys
from lib.control_flow import calculator
def test_prints_invalid_returns_none_if_invalid(self):
    """prints "Error: Invalid operation!" and returns None if operation invalid"""
    captured_out = io.StringIO()       # Capture standard output
    sys.stdout = captured_out           # Redirect standard output to captured_out
    result = calculator('a', 1, 2)       # Call calculator with invalid operation
    sys.stdout = sys.__stdout__        # Restore standard output
    assert result is None              # Check that it returns None
    assert captured_out.getvalue() == "Error: Invalid operation!\n"  # Check error message
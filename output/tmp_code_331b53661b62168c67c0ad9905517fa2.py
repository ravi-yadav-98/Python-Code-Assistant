def factorial(n):
    if isinstance(n, int) and n >= 0:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    else:
        raise ValueError("Input must be a non-negative integer.")


# Example usage:
try:
    num = int(input("Enter a non-negative integer: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
except ValueError as e:
    print("Invalid input. Please enter a valid non-negative integer.")
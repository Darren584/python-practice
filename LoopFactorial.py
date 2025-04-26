# Function to compute factorial using a loop
def factorial_loop(n):
    result = 1  # Start with result 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by each number up to n
    return result  # Return the factorial

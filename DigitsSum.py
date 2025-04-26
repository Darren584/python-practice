# Function to sum the digits of a number
def sum_of_digits(n):
    total = 0  # Initialize sum to zero
    while n > 0:
        digit = n % 10  # Get the last digit
        total += digit  # Add digit to total
        n = n // 10  # Remove the last digit
    return total  # Return the total sum

# Example usage:
# print(sum_of_digits(123))  # Output: 6

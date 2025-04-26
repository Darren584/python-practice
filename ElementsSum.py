# Function to sum all elements in a list
def sum_list(numbers):
    total = 0  # Initialize total to zero
    for num in numbers:
        total += num  # Add each number to total
    return total  # Return the final sum

# Example usage:
# print(sum_list([1, 2, 3, 4]))  # Output: 10

# Function to reverse a string manually
def reverse_string(s):
    reversed_str = ''  # Empty string to store reversed characters
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character
    return reversed_str  # Return the reversed string

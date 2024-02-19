def binary_to_decimal(binary):
  """Converts an 8-bit binary number to decimal.

  Args:
    binary: A string representing the 8-bit binary number.

  Returns:
    The decimal equivalent of the binary number.
  """

  decimal = 0
  for digit in binary:
    decimal = decimal * 2 + int(digit)
  return decimal


# Example usage:

binary = "10011010"
decimal = binary_to_decimal(binary)
print(decimal)  # Prints 154
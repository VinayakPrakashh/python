class CustomError(Exception):
    """Custom exception class."""
    
    def __init__(self, message="A custom error occurred."):
        self.message = message
        super().__init__(self.message)

# Example of using the custom exception
def example_function(value):
    if value < 0:
        raise CustomError("Negative values are not allowed.")

# Using the custom exception in your code
try:
    user_input = int(input("Enter a positive number: "))
    example_function(user_input)
except CustomError as ce:
    print(f"CustomError: {ce}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
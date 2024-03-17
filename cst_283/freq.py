def frequency(input_string):
    # Convert the input string to lowercase
    input_string = input_string.lower()

    # Initialize an empty dictionary to store the frequency of each letter
    letter_frequency = {}

    # Calculate the frequency of each letter in the input string
    for char in input_string:
        if char.isalpha():
            if char in letter_frequency:
                letter_frequency[char] += 1
            else:
                letter_frequency[char] = 1

    # Sort the dictionary by value in non-increasing order
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

    # Print the letters in non-increasing order of their frequency
    for char, frequency in sorted_frequency:
        print(f"{char}: {frequency}")

# Test the function with an example string
input_string = "Hello, World!"
print("Frequency of letters in non-increasing order:")
frequency(input_string)

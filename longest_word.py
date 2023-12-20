def find_longest_word(text):
    words = text.split()  # Split the text into words

    # Find the longest word using a concise approach
    longest_word = max(words, key=len)

    return longest_word

# Get input from the user
text_input = input("Enter a sentence or text: ")

# Find the longest word
longest_word = find_longest_word(text_input)

# Print the result in a user-friendly format
print(f"The longest word in your text is '{longest_word}' with a length of {len(longest_word)} characters.")

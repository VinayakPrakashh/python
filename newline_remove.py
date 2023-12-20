def remove_newlines(filename):
    with open(filename, 'r') as input_file:
        contents = input_file.read()

    contents_without_newlines = contents.replace('\n', '')

    with open(filename, 'w') as output_file:
        output_file.write(contents_without_newlines)

# Example usage
filename = 'your_file.txt'  # Replace with the actual filename
remove_newlines(filename)

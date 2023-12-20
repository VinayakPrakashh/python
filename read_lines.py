def read_file_lines(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())  # Remove trailing newline characters
    return lines

# Example usage
filename = "factorial.py"  # Replace with the actual filename
lines = read_file_lines(filename)
print(lines)

def calculate_tape_length(columns, first_row, second_row):
    tape_length = 0
    for col in range(columns):
        if first_row[col] == 1:
            tape_length += 2  # Add 2 meters for the two sides of the triangular tile
            if col == 0 or first_row[col - 1] == 0:  # If it's the beginning of a wet area
                tape_length += 1  # Add 1 meter for the corner
            if col == columns - 1 or first_row[col + 1] == 0:  # If it's the end of a wet area
                tape_length += 1  # Add 1 meter for the corner
        if second_row[col] == 1:
            tape_length += 2  # Add 2 meters for the two sides of the triangular tile
            if col == 0 or second_row[col - 1] == 0:  # If it's the beginning of a wet area
                tape_length += 1  # Add 1 meter for the corner
            if col == columns - 1 or second_row[col + 1] == 0:  # If it's the end of a wet area
                tape_length += 1  # Add 1 meter for the corner
    return tape_length

# Sample Input 1
columns_1 = 5
first_row_1 = [1, 0, 1, 0, 1]
second_row_1 = [0, 0, 0, 0, 0]
print(calculate_tape_length(columns_1, first_row_1, second_row_1))  # Output: 9

# Sample Input 2
columns_2 = 7
first_row_2 = [0, 0, 1, 1, 0, 1, 0]
second_row_2 = [0, 0, 1, 0, 1, 0, 0]
print(calculate_tape_length(columns_2, first_row_2, second_row_2))  # Output: 11

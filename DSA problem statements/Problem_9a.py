from itertools import permutations

def is_magic(square):
    # Check rows and columns
    for i in range(3):
        if sum(square[i]) != 15:  # Row sum
            return False
        if sum(square[j][i] for j in range(3)) != 15:  # Column sum
            return False

    # Check diagonals
    if square[0][0] + square[1][1] + square[2][2] != 15:
        return False
    if square[0][2] + square[1][1] + square[2][0] != 15:
        return False

    return True

def find_magic_square():
    digits = list(range(1, 10))
    for perm in permutations(digits):
        square = [list(perm[i:i+3]) for i in range(0, 9, 3)]
        if is_magic(square):
            return square  # Return the first magic square found
    return None

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Example usage
magic = find_magic_square()
if magic:
    print("MAGIC SQUARE:")
    print_grid(magic)
else:
    print("No magic square found.")

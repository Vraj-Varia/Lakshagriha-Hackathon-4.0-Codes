def generate_pseudo_magic_block():
    # A 3x3 block where row/column sums = 15, but diagonal sums can differ
    return [
        [4, 5, 6],
        [6, 5, 4],
        [5, 5, 5]
    ]

def tile_pseudo_magic_square(n):
    if n < 3:
        raise ValueError("n must be >= 3")
    block = generate_pseudo_magic_block()
    grid = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = block[i % 3][j % 3]
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

n = 6  # You can change this to any n >= 3
pseudo_magic_square = tile_pseudo_magic_square(n)
print(f"\n{n}x{n} Pseudo-Magic Square (3x3 blocks):")
print_grid(pseudo_magic_square)

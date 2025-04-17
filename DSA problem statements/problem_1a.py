def max_coins_path(grid):
    if not grid:
        return 0, []
    
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    path = [[[] for _ in range(cols)] for _ in range(rows)]
    
    dp[0][0] = grid[0][0]
    path[0][0] = [(0, 0)]
    
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        path[0][j] = path[0][j-1] + [(0, j)]
    
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        path[i][0] = path[i-1][0] + [(i, 0)]
    
    for i in range(1, rows):
        for j in range(1, cols):
            if dp[i-1][j] + grid[i][j] > dp[i][j-1] + grid[i][j]:
                dp[i][j] = dp[i-1][j] + grid[i][j]
                path[i][j] = path[i-1][j] + [(i, j)]
            else:
                dp[i][j] = dp[i][j-1] + grid[i][j]
                path[i][j] = path[i][j-1] + [(i, j)]
    
    return dp[rows-1][cols-1], path[rows-1][cols-1]

grid = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0]
]

max_coins, path = max_coins_path(grid)
print(f"Maximum coins: {max_coins}")
print(f"Path: {path}")

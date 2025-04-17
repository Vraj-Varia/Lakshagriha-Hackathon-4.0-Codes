import time
import os

# Neighbor offsets (8 directions)
NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),          (0, 1),
             (1, -1),  (1, 0), (1, 1)]

def print_board(live_cells, gen, size=10):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Generation {gen}")
    for y in range(-size, size):
        row = ''
        for x in range(-size, size):
            row += '#' if (x, y) in live_cells else '.'
        print(row)
    time.sleep(0.5)

def next_generation(live_cells):
    from collections import defaultdict
    neighbor_count = defaultdict(int)
    
    # Count live neighbors for each cell
    for (x, y) in live_cells:
        for dx, dy in NEIGHBORS:
            neighbor_count[(x + dx, y + dy)] += 1

    new_live_cells = set()
    for cell, count in neighbor_count.items():
        if count == 3 or (count == 2 and cell in live_cells):
            new_live_cells.add(cell)
    
    return new_live_cells

# === CONFIGURATIONS === #

def get_block():
    return {(0, 0), (0, 1), (1, 0), (1, 1)}  # Still life

def get_blinker():
    return {(0, 0), (1, 0), (2, 0)}  # Oscillator

def get_glider():
    return {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}  # Spaceship

# === MAIN SIMULATION === #

def simulate(config_func, generations=10, size=10):
    live_cells = config_func()
    for gen in range(generations):
        print_board(live_cells, gen, size)
        live_cells = next_generation(live_cells)

# === RUN SIMULATIONS === #
if __name__ == "__main__":
    print("Choose configuration to simulate:")
    print("1. Still Life (Block)")
    print("2. Oscillator (Blinker)")
    print("3. Spaceship (Glider)")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        simulate(get_block, generations=10)
    elif choice == '2':
        simulate(get_blinker, generations=10)
    elif choice == '3':
        simulate(get_glider, generations=20)
    else:
        print("Invalid choice.")
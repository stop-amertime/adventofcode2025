grid = [list(l.strip()) for l in open("test_input.txt")]

w, h = len(grid), len(grid[0])

is_valid           = lambda x,y: 0 <= x < w and 0 <= y < h
is_roll            = lambda x,y: is_valid(x,y) and grid[x][y] == "@"
rolls_in_3x3       = lambda x,y: sum(is_roll(x+dx,y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1])
is_accessible_roll = lambda x,y: is_roll(x,y) and rolls_in_3x3(x,y) < 5

def remove_accessible_rolls():
    to_remove = [(x,y) for x in range(w) for y in range(h) if is_accessible_roll(x,y)] 

    if not to_remove: 
        return 0

    for x, y in to_remove:
        grid[x][y] = "."
    
    return len(to_remove) + remove_accessible_rolls()

print(remove_accessible_rolls())
test_input = [l.strip() for l in open("test_input.txt")]

w, h = len(test_input), len(test_input[0])

is_valid        = lambda x,y:   0 <= x < w and 0 <= y < h
is_roll         = lambda x,y:   is_valid(x,y) and test_input[x][y] == "@"
rolls_in_3x3    = lambda x,y:   sum(is_roll(x+dx,y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1])

print(sum(
        cell == "@" and rolls_in_3x3(x,y) < 5
            for x, row in enumerate(test_input) for y, cell in enumerate(row)
    ))

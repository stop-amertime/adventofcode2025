if __name__ == "__main__":

    test_array = "L68 L30 R48 L5 R60 L55 L1 L99 R14 L82".split(" ")
    strings = []
    with open('day-1/puzzle-input.txt', 'r') as file:
        strings = [line.strip() for line in file.readlines()]

    ## Start pointing at 50
    pos = 50
    zero_visits = 0

    ## Manually increment/decrement and track visits to position 0
    for command in strings:
        for i in range(int(command[1:])):
            pos += 1 if command[0] == 'R' else -1
            pos = pos % 100
            if pos == 0: zero_visits += 1
    
    print(f"Number of visits to position 0: {zero_visits}")

        
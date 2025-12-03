with open("input.txt") as f:
    test = [line.strip() for line in f.readlines()]

JOLTAGE_LENGTH = 12
total_joltage = 0

if __name__ == "__main__":
    for bank in test:

        digits, search_start =  [], 0
        
        for position in range(JOLTAGE_LENGTH):
            search_space = bank[search_start : -(JOLTAGE_LENGTH-position-1) or None]
            digits.append(max(search_space))
            search_start = search_start + search_space.index(digits[-1]) + 1
        
        total_joltage += int(''.join(digits))
    
    print(total_joltage)

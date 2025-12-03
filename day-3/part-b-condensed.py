def find_joltage(bank):
    digits, search_start =  [], 0
    for pos in range(12):

        # Search space is from current search start to the position where remaining digits fit
        search_space = bank[search_start : -(11-pos) or None]

        # Get the max digit in the current search space
        digits.append(max(search_space))

        # Update search start to one position after the found digit
        search_start = search_start + search_space.index(digits[-1]) + 1

    return ''.join(digits)

print(
    sum(int(find_joltage(bank.strip()))
        for bank in open("input.txt")
    )
)
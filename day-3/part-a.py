with open("input.txt") as f:
    test = [line.strip() for line in f.readlines()]
    print(test)
total_joltage = 0

if __name__ == "__main__":
    for bank in test:

        first_digit = max(int(digit) for digit in bank[:-1])
        second_digit = max(int(digit) for digit in bank[bank.index(str(first_digit))+1:])
        total_joltage += first_digit*10 + second_digit
    
    print(total_joltage)
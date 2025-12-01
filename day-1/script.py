## python script that loads an array of strings from a text file into a list
def load_strings_from_file(file_path):
    with open(file_path, 'r') as file:
        strings_list = [line.strip() for line in file.readlines()]
    return strings_list

test_array = "L68 L30 R48 L5 R60 L55 L1 L99 R14 L82".split(" ")

if __name__ == "__main__":
    file_path = 'puzzle-input.txt'  
    strings = load_strings_from_file(file_path)
    pos = 50
    zero_visits = 0
    for command in strings:
        print(f"Processing command: {command}, direction: {command[0]}, value: {int(command[1:])}")
        for i in range(int(command[1:])):
            pos += 1 if command[0] == 'R' else -1
            pos = pos % 100
            if pos == 0: zero_visits += 1
    print(f"Number of visits to position 0: {zero_visits}")


        
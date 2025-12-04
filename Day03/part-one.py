handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

## each row of digits is a bank of batteries
## within each bank we need to turn on _exactly_ two batteries
## the JOLTAGE produced is the two digits from left to right
## e.g. bank 12345, turn on 2 and 4, joltage is 24 (no re-arranging)

## Task - find the largest joltage each bank can produce, return value of total max joltage of all banks
total_max_joltage = 0

for bank in data:
    ## split digits into a list
    batteries = list(map(int, bank))
    print(batteries)
    ## we can ignore the last digit for the tens digit
    last = batteries.pop()
    ## figure out biggest one remaining
    tens_digit = max(batteries)
    print(tens_digit)

    ## locate the earliset position of our tens digit (most options for ones digit)
    tens_position = bank.find(str(tens_digit))

    ## cut the string short from there (character after, so pos + 1)
    cut_string = bank[tens_position + 1:]

    ## repeat the "find the biggest" logic
    ones_candidates = list(map(int, cut_string))
    print(ones_candidates)
    ## figure out biggest one remaining
    ones_digit = max(ones_candidates)
    print(ones_digit)

    ## convert digits to real numbers
    joltage = int(str(tens_digit) + str(ones_digit))
    print("Joltage: " + str(joltage))

    ## add to total
    total_max_joltage = total_max_joltage + joltage

print("Total Max Joltage: " + str(total_max_joltage))
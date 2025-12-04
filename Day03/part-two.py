handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

## each row of digits is a bank of batteries
## within each bank we need to turn on _exactly_ twelve batteries
## the JOLTAGE produced is the twelve digits from left to right

## Task - find the largest joltage each bank can produce, return value of total max joltage of all banks
total_max_joltage = 0

def find_biggest_with_scopes(bank, digit_index):
    ## don't mess with it if we only need one
    if digit_index <= 1:
        batteries = bank
    else:
        ## otherwise remove digits we can't choose from the end
        batteries = bank[:-(digit_index - 1)]

    # print(batteries)

    ## convert to array for max comparison
    batteries = list(map(int, batteries))
    biggest = max(batteries)

    ## look up position on original input string
    biggest_pos = bank.find(str(biggest))

    # print("Biggest is: " + str(biggest))
    # print("Biggest pos is: " + str(biggest_pos))
    return biggest, biggest_pos


for bank in data:

    biggest_pos = -1
    joltage = ''
    candidate_str = bank

    ## we want twelve digits, so walk our way down
    for i in range(12, 0, -1):
        ## update our string to start from the position we found in the last loop
        candidate_str = candidate_str[biggest_pos + 1:]
        # print("i is: " + str(i))
        # print("candidate_str is:" + candidate_str)
        
        ## if we need i digits and we only have i left, use them all!
        if len(candidate_str) == i:
            joltage = joltage + candidate_str
            print("Joltage: " + str(joltage))
            break
        
        ## call the magic function
        biggest, biggest_pos = find_biggest_with_scopes(candidate_str, i)
        
        ## add strings to simulate digits
        joltage = joltage + str(biggest)
        print("Joltage: " + str(joltage))

    ## add to total (this time, maths)
    total_max_joltage = total_max_joltage + int(joltage)

print("Total Max Joltage: " + str(total_max_joltage))
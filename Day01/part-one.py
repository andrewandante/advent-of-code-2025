handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

dial = 50
zero_count = 0

for rotation in data:
    # print(rotation)
    # first character tells us the direction to turn 
    direction = rotation[0]
    # remaining characters tell us how far to turn
    amount = int(rotation[1:])

    if direction == 'L':
        # should be negative
        dial = dial - amount
        ## make sure this is still on the dial
        while dial < 0:
            dial = dial + 100
    elif direction == 'R':
        # should be positive
        dial = dial + amount
        ## make sure this is still on the dial
        while dial > 99:
            dial = dial - 100
    else:
        print("Everything is broken I guess")

    # print("Dial is at: " + str(dial))
    if dial == 0:
        # it's pointing at zero! count it!
        zero_count = zero_count + 1
        # print("Zero count is: " + str(zero_count))

print("Final Zero count is: " + str(zero_count))
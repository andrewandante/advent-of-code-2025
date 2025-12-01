handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

dial = 50
zero_count = 0

for rotation in data:
    print(rotation)
    # first character tells us the direction to turn 
    direction = rotation[0]
    # remaining characters tell us how far to turn
    amount = int(rotation[1:])

    while amount > 99:
        # reduce the larger numbers down to smaller increments here
        amount = amount - 100
        # count each one of these as a full turn
        zero_count = zero_count + 1
        print("[REDUCE] Zero count is: " + str(zero_count))

    
    if direction == 'L':
        # we should increment zero count if a) the dial hasn't started at zero (already counted) and b) this will take us below zero
        if dial != 0 and dial - amount <= 0:
            zero_count = zero_count + 1
            print("[L] Zero count is: " + str(zero_count))

        # L means negative
        dial = dial - amount
        if dial < 0:
            dial = dial + 100
        print("Dial now reads: " + str(dial))
    elif direction == 'R':
        # we should increment zero count if a) the dial hasn't started at zero (already counted) and b) this will take us above 99
        if dial != 0 and dial + amount > 99:
            zero_count = zero_count + 1
            print("[R] Zero count is: " + str(zero_count))
        # should be positive
        dial = dial + amount
        if dial > 99:
            dial = dial - 100
        ## make sure this is still on the dial
        print("Dial now reads: " + str(dial))
    else:
        print("Everything is broken I guess")

print("Final Zero count is: " + str(zero_count))
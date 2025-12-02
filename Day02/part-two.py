handle = open("input.txt", "r")
# this data is a single line, comma-separated
data = handle.read().split(',')
handle.close()

## data is a list of ranges: start-end
## invalid ranges are _at-least_ twice-repeated digit-sequences ie 11, 121212, 123123123123
## task is to sum up the invalid ids
id_sum = 0

for id_range in data:
    start, end = id_range.split('-')
    # print("Start is: " + str(start))
    # print("End is: " + str(end))

    ## need to include the end value so add the + 1
    for candidate in range(int(start), int(end) + 1, 1):
        should_add = True
        # print("Assessing " + str(candidate))

        ## we want to loop through prime numbers up to the length of the string
        ## this is find the lowest common factor we can split by
        candidate_len = len(str(candidate))

        for factor in range(2, candidate_len + 1):
            ## gunna hard-code in primes cos who cares
            if factor not in (2,3,5,7,11,13,17,19,23,29):
                # print("Not a prime factor, skipping")
                continue

            should_add = True
            ## if the length is divides neatly into the prime, we can check by comparing the splits
            if candidate_len % factor == 0:
                # print("Even divider, comparing splits")
                ## the function below splits into pieces all of n size - so we do the division here to match
                ## we know that it will divide nicely from the modulus check above
                divider = int(candidate_len / factor)
                ## split the string into pieces
                ## borrowed from here: https://stackoverflow.com/questions/22571259/split-a-string-into-n-equal-parts
                parts = list(map(''.join, zip(*[iter(str(candidate))]*divider)))
                # print("Parts: " + str(parts))
                first = parts[0]
                for part in parts:
                    ## loop through each piece, if any of them don't match the first piece we can move on
                    if part != first:
                        should_add = False
                        # print("Parts don't match, skipping")
                        break
                if should_add == True:
                    print("All parts match - adding to total")
                    print("Adding " + str(candidate))
                    id_sum = id_sum + candidate
                    print("Updated total: " + str(id_sum))
                    ## break away here, we don't need to keep going if we've established it meets the criteria
                    break

print("Final total: " + str(id_sum))    
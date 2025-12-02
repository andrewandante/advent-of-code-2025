handle = open("input.txt", "r")
# this data is a single line, comma-separated
data = handle.read().split(',')
print(data)
handle.close()

## data is a list of ranges: start-end
## invalid ranges are _exactly_ twice-repeated digit-sequences ie 11, 1212, 123123
## task is to sum up the invalid ids
id_sum = 0

for id_range in data:
    start, end = id_range.split('-')
    print("Start is: " + str(start))
    print("End is: " + str(end))

    ## need to include the end value so add the + 1
    for candidate in range(int(start), int(end) + 1, 1):
        print("Assessing " + str(candidate))
        ## if the length is not even, it can't be a twice-repeated sequence
        candidate_len = len(str(candidate))
        if candidate_len % 2 != 0:
            print("Not even length, skipping")
            continue
        ## split the string by half the length, first front and then back
        ## borrowed from here: https://stackoverflow.com/questions/4789601/split-a-string-into-2-in-python
        first_half, second_half = str(candidate)[:candidate_len//2], str(candidate)[candidate_len//2:]
        if first_half != second_half:
            print("Halves don't match, skipping")
            continue
        print("Matches invalid ID criteria - adding to total")
        id_sum = id_sum + candidate
        print("Updated total: " + str(id_sum))

print("Final total: " + str(id_sum))
    
handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

## The database consists of a list of fresh ingredient ID ranges;
## a blank line, and a list of available ingredient IDs.

fresh_ranges = []
fresh_count = 0

for line in data:
    if '-' in line:
        ## this is a range - find the start and end
        start, end = line.split('-')
        ## collect these in a list
        fresh_ranges.append((int(start), int(end)))
        continue

## now eliminate overlaps
fresh_ranges = list(set(fresh_ranges))

## start by sorting
fresh_ranges.sort()


## start our useables with the first
usable_ranges = [
    fresh_ranges.pop(0)
]

for can_start, can_end in fresh_ranges:
    compare_range = usable_ranges[-1]
    ## if it starts inside the previous range
    if can_start <= compare_range[1]:
        ## replace the end of the previous range with whichever end is bigger
        usable_ranges[-1] = (compare_range[0], max(compare_range[1], can_end))
    else:
        ## otherwise, it's our new most biggest range
        usable_ranges.append((can_start, can_end))

# print(usable_ranges)
for start, end in usable_ranges:
    ## do math on each range
    fresh_count_increase = (end + 1) - start
    fresh_count = fresh_count + fresh_count_increase

print(f"Fresh count is {fresh_count}")

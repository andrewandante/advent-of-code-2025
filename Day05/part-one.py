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
    elif line != '':
        ## now we are up to ingredients
        for range_start, range_end in fresh_ranges:
            ## if it sits inside a range, count it!
            if int(line) >= range_start and int(line) <= range_end:
                fresh_count = fresh_count + 1
                break

print(f"Fresh count is {fresh_count}")

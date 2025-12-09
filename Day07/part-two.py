handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

## use the first line to set up columns
calibrator = data[0]
current_line = []
next_line = []

## there's definitely a better way to do this
## preload our path counts with zero
for column in enumerate(calibrator):
    current_line.append(0)
    next_line.append(0)


for row_index, row in enumerate(data):
    for index, column in enumerate(row):
        ## in here, we determine we have 1 path exactly
        if column == 'S':
            next_line[index] = next_line[index] + 1
            continue

        ## here we just pass the path count down to the next line
        if column == '.':
            next_line[index] = next_line[index] + current_line[index]
            continue

        ## on a splitter
        if column == '^':
            ## if this isnt hard left, add path count to the left
            if index > 0:
                next_line[index - 1] = next_line[index - 1] + current_line[index]
            ## if this isn't hard right, add path count to the right
            if index < (len(row) - 1):
                next_line[index + 1] = next_line[index + 1] + current_line[index]
            continue
    ## at the end of the row, load "next" into current and make "next" empty
    for col_index, col in enumerate(next_line):
        current_line[col_index] = col
        next_line[col_index] = 0

## Print out the "valid paths that end here" count for the last line
print(f"Final line looks like this")
print(current_line)

## Sum them up
print(f"Total is {sum(current_line)}")
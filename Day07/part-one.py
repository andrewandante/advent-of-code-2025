handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

## use the first line to set up columns and starting point
calibrator = data.pop(0)
columns = {}
split_count = 0

## there's definitely a better way to do this
for index, column in enumerate(calibrator):
    if column == '.':
        columns[index] = ['.']
    elif column == 'S':
        columns[index] = ['S']


for row in data:
    skip = False
    for index, column in enumerate(row):
        ## we skip if the splitter has already set the next row for us
        if skip == True:
            skip = False
            continue
        ## check above
        above = columns[index][-1]
        if column == '.':
            ## if a dot, just put a new dot if above was a dot or a split
            if above == '^' or above == '.':
                columns[index].append('.')
            ## otherwise it was a ray we should continue with
            elif above == 'S' or above == '|':
                columns[index].append('|')
        ## on a splitter, split if there was a ray coming in
        elif column == '^':
            if above == '|':
                ## split it - set previous and next
                columns[index - 1][-1] = '|'
                columns[index + 1].append('|')
                ## make sure we don't run the next char as we've already set it
                skip = True
                split_count = split_count + 1
            ## either way, shove the splitter into the diagram
            columns[index].append('^')
            
## render (optional)
for i in range(len(calibrator) + 1):
    line = ''
    for column in columns.values():
        line = line + column[i]
    print(line)
    
print(f"Split count is {split_count}")
handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

map = {}
row_count = 0
roll_count = 0

def check_adjacent_cells(row, column):
    ## provide list of indices to nudge by to check adjacent cells
    adjacents = [
        [-1, -1],[-1, 0],[-1, 1],[0, -1], [0, 1], [1, -1],[1, 0],[1, 1]
    ]
    max_adj = 4
    adj_count = 0

    ## loop over candidates
    for adj in adjacents:
        adj_row, adj_col = adj

        ## add current row with nudge
        candidate_row = row + adj_row
        ## skip if we've gone outside the box
        if candidate_row not in map.keys():
            continue
        ## repeat for columns
        candidate_col = column + adj_col
        if candidate_col < 0 or candidate_col >= len(map[candidate_row]):
            continue

        ## get value of adjacent cell
        neighbour = map[candidate_row][candidate_col]
        ## if also a roll of paper increment count
        if neighbour == '@':
            adj_count = adj_count + 1
            ## if we've reached the max, bail out
            if adj_count >= max_adj:
                return False

    ## otherwise we are fine!
    return True

## convert to a grid for processing
for line in data:
    map[row_count] = list(line)
    row_count = row_count + 1

## loop over each row
for row_number, row in map.items():
    ## loop over each item in each row
    for index, item in enumerate(row):
        ## only act if it's a roll
        if item == '@':
            if check_adjacent_cells(row_number, index) == True:
                roll_count = roll_count + 1

print("Roll count: " + str(roll_count))
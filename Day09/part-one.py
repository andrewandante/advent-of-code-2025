handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

red_tiles = {}
biggest_area = 0

## convert each line into x,y,z co-ordinates
for index, coordinates in enumerate(data):
    red_tiles[index] = list(map(int, coordinates.split(',')))

def calculate_area(pointa, pointb):
    length = abs(pointa[0] - pointb[0]) + 1
    width = abs(pointa[1] - pointb[1]) + 1

    return length * width

## calculate all distances and order
for index, tile in red_tiles.items():
    for oindex, otile in red_tiles.items():
        ## don't duplicate co-ordinates
        if index >= oindex:
            continue
        area = calculate_area(tile, otile)
        if area > biggest_area:
            biggest_area = area


print(f"Area is {biggest_area}")

## 4442262383 is too low
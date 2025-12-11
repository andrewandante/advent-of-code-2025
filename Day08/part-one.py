import numpy as np

handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

junction_boxes = {}
used_circuits = []
circuits = {}

distances_map = {}

## convert each line into x,y,z co-ordinates
for index, coordinates in enumerate(data):
    junction_boxes[index] = list(map(int, coordinates.split(',')))
    ## preload the circuits
    circuits[index] = [index]

def numpy_euclidean_distance(point1, point2):
    """Calculates the Euclidean distance using NumPy's linalg.norm."""
    p1_array = np.array(point1)
    p2_array = np.array(point2)
    # Calculate the L2 norm (Euclidean distance) of the difference vector
    distance = np.linalg.norm(p1_array - p2_array)
    return distance

# print(junction_boxes)

## calculate all distances and order
for index, jb in junction_boxes.items():
    for oindex, ojb in junction_boxes.items():
        ## don't duplicate co-ordinates
        if index >= oindex:
            continue
        distances_map[(index, oindex)] = numpy_euclidean_distance(jb, ojb)

## sort by distances asc
sorted_distances = dict(sorted(distances_map.items(), key=lambda item: item[1]))

## use range(1, 11) for the example input
for i in range(1, 1001):
    ## get next key
    shortest_pair = next(iter(sorted_distances.keys()))
    ## pop it off
    sorted_distances.pop(shortest_pair)

    positiona = -1
    positionb = -1

    ## go find our boxes in the circuits
    for cand_index, cand_circuit in circuits.items():
        if shortest_pair[0] in cand_circuit:
            positiona = cand_index
        if shortest_pair[1] in cand_circuit:
            positionb = cand_index

    ## if they are already a pair, hooray! keep going
    if positiona == positionb:
        continue

    ## otherwise move all from one onto the other
    toMove = circuits.pop(positiona)
    circuits[positionb] = circuits[positionb] + toMove

## Sort the circuits by length
sorted_circuits = dict(sorted(circuits.items(), key=lambda item: len(item[1]), reverse=True))

## do math
loops = 0
total = 1
for sorted in sorted_circuits.values():
    total = total * len(sorted)
    loops = loops + 1
    ## only need the top 3
    if loops == 3:
        break

print(f"Total product: {total}")

## 4290 too low
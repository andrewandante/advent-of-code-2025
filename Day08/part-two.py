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

## know how long our circuit will be with everyone in it
full_circuit_length = len(circuits)

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

## loop until we are done
complete = False
while complete == False:
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
    ## we should have the full lot here now
    if len(circuits[positionb]) >= full_circuit_length:
        complete = True

## do math
firstx = junction_boxes[shortest_pair[0]][0]
secondx = junction_boxes[shortest_pair[1]][0]
total = firstx * secondx

print(f"Total product: {total}")
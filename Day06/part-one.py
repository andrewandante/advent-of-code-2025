import math

handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

columns = {}
grand_total = 0

## break off the operators first
operators = data.pop().split()
for index, operator in enumerate(operators):
    columns[index] = [operator]

for line in data:
    items = line.split()
    ## fix the data into columns instead of rows
    for index, item in enumerate(items):
        columns[index].append(int(item))

for column in columns.values():
    ## pop the operator back off
    operator = column.pop(0)
    ## use the appropriate method to determine the total to use
    if operator == '+':
        grand_total = grand_total + sum(column)
    else:
        grand_total = grand_total + math.prod(column)

print(f"Grand total is {grand_total}")

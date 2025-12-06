import math

handle = open("input.txt", "r")
data = handle.read().splitlines()
handle.close()

columns = {}
grand_total = 0

for line in data:
    ## fix the data into columns instead of rows
    for index, character in enumerate(list(line)):
        if index not in columns:
            columns[index] = [character]
        else:
            columns[index].append(character)

operator = ''
values_to_process = []

for column in columns.values():

    if operator == '':
        ## pop the operator off
        operator = column.pop()
    
    ## remove empty strings
    col_digits = list(filter(None, [s.replace(" ", "") for s in column]))

    ## this means we've hit a break column, and need to perform the operation
    if len(col_digits) == 0:
        ## use the appropriate method to determine the total to use
        if operator == '+':
            grand_total = grand_total + sum(values_to_process)
        else:
            grand_total = grand_total + math.prod(values_to_process)
        operator = ''
        values_to_process = []
        continue

    ## convert to string
    col_string = "".join(col_digits)
    ## add int to the pile for processing later
    values_to_process.append(int(col_string))

## Get the last one
if operator == '+':
    grand_total = grand_total + sum(values_to_process)
else:
    grand_total = grand_total + math.prod(values_to_process)

print(f"Grand total is {grand_total}")

# Advent of Code: 2025

## Getting started

For each day, copy the Day00 directory over for a new day.

Paste the example input into `exampleinput.txt` so you can test your solution against the example in the question.

Paste your puzzle input into `input.txt` figuring out the answers.

Run `python part-one.py` to execute

## Defaults

By default, the script will simply echo the `data` it reads from the `exampleinput.txt` file, separating each line into an item into an array:

```py
handle = open("input.txt", "r")
data = handle.read().splitlines()
print(data)
handle.close()
```

If instead you want to separate on commas, try:

```py
handle = open("exampleinput.txt", "r")
data = handle.read().split(',')
print(data)
handle.close()
```
handle = open("exampleinput.txt", "r")
# this data is a single line, comma-separated
data = handle.read().split(',')
handle.close()


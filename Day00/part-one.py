handle = open("exampleinput.txt", "r")
data = handle.read().splitlines()
print(data) 
handle.close()
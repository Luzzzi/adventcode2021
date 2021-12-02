with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]

command = 0
horizontal_position = 0
depth = 0
for i in range(0, len(lines)):
    command = lines[i].split()
    print(command)
    for i in range (len(command)-1):
        if command[i] == "forward":
            horizontal_position += int(command[i +1])
        if command[i] == "down":
            depth += int(command[i+1])
        if command[i] == "up":
            depth -= int(command[i+1])

final_position = depth * horizontal_position
print(final_position)
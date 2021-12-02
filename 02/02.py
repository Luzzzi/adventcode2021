with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]

command = 0
horizontal_position = 0
depth = 0
for i in range(0, len(lines)):
    command = lines[i].split()
    if command[0] == "forward":
        horizontal_position += int(command[1])
    if command[0] == "down":
        depth += int(command[1])
    if command[0] == "up":
        depth -= int(command[1])

final_position = depth * horizontal_position
print(final_position)
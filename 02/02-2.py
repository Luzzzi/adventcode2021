with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]

command = 0
horizontal_position = 0
depth = 0
aim = 0
for i in range(0, len(lines)):
    command = lines[i].split()
    if command[0] == "forward":
        horizontal_position += int(command[1])
        depth += aim * int(command[1])
    if command[0] == "down":
        aim += int(command[1])
    if command[0] == "up":
        aim -= int(command[1])

final_position = depth * horizontal_position
print(final_position)
with open("input2.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]

command = 0
horizontal_position = 0
depth = 0
aim = 0
for i in range(0, len(lines)):
    command = lines[i].split()
    print(command)
    for i in range (len(command)-1):
        if command[i] == "forward":
            horizontal_position += int(command[i +1])
            depth = depth * aim
        if command[i] == "down":
            depth += int(command[i+1])
            aim += int(command[i]+1)
        if command[i] == "up":
            depth -= int(command[i+1])
            aim -= int(command)

print(depth)
print(horizontal_position)
final_position = depth * horizontal_position
print(final_position)
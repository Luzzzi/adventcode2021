with open("input2.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]


initial_state = lines[0].split(",")
initial_state = [int(i) for i in initial_state]
fish = 0
days = 80

for day in range(days):
    for i in range(len(initial_state)):
        if initial_state[i] > 0: 
            initial_state[i] -= 1
        else:
            initial_state[i] += 6
            initial_state.append(8)
    print(day -1)


fish = len(initial_state)
print(fish)
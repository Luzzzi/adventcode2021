with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]


initial_state = lines[0].replace(",", "")
initial_state = [int(i) for i in initial_state]
days = 0
fish = 0

while days < 80: 
    days += 1
    print("After", days -1, "day")
    print(initial_state)
    for i in range(len(initial_state)):
        if initial_state[i] <= 8 and initial_state[i] > 0: 
            initial_state[i] -= 1
        elif initial_state[i] == 0: 
            initial_state[i] += 6
            initial_state.append(8)

fish = len(initial_state)
print(fish)
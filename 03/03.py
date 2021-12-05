with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]

gamma_rate = []
epsilon_rate = []


def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s), 2)
      
    return(res)


for j in range (len(lines[0])):
    counter_zero = 0
    counter_one = 0 
    for i in range(len(lines)): 
        if lines[i][j] == "1": 
            counter_one += 1
        else:
            counter_zero += 1 
    
    if counter_one > counter_zero: 
        gamma_rate.append(1)
        epsilon_rate.append(0)
    if counter_one < counter_zero:
        gamma_rate.append(0)
        epsilon_rate.append(1)


power_consumption = (convert(gamma_rate)) * (convert(epsilon_rate))

print(power_consumption)
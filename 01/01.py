with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]

for i in range(len(lines)):
    lines[i] = int(lines[i])

counter = 0
sum = []

for i in range(len(lines)-2):
    sum.append(lines[i] + lines[i+1] + lines[i+2])  

for i in range(len(sum)-1):
    if sum[i] < sum[i+1]:
        counter +=1

print(sum)
print(counter)
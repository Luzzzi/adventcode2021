with open("input.txt", "r") as fd:
    lines = fd.readlines()
    lines = [line.rstrip() for line in lines]

list_oxygen = lines
list_CO2 = lines
oxygen_rating = 0
CO2_rating = 0

#Convert binary into integer 
def convert(list):
      
    # Converting integer list to string list
    s = [str(i) for i in list]
      
    # Join list items using join()
    res = int("".join(s), 2)
      
    return(res)

#Oxygen generator Rating 
for j in range (len(list_oxygen[0])):
    counter_zero = 0
    counter_one = 0 
    list_zero = []
    list_one = []

    for i in range(len(list_oxygen)): 
        if list_oxygen[i][j] == "1": 
            counter_one += 1
            list_one.append(list_oxygen[i])
        else:
            counter_zero += 1 
            list_zero.append(list_oxygen[i])
    
    if counter_one > counter_zero: 
        list_oxygen = list_one
    elif counter_one < counter_zero:
        list_oxygen = list_zero
    else:
        list_oxygen = list_one 

    if len(list_oxygen) == 1:
        break

oxygen_rating = convert(list_oxygen)

#CO2 scrubber Rating 
for j in range (len(list_CO2[0])):
    counter_zero = 0
    counter_one = 0 
    list_zero = []
    list_one = []

    for i in range(len(list_CO2)): 
        if list_CO2[i][j] == "1": 
            counter_one += 1
            list_one.append(list_CO2[i])
        else:
            counter_zero += 1 
            list_zero.append(list_CO2[i])

    if counter_one < counter_zero: 
        list_CO2 = list_one
    elif counter_one > counter_zero:
        list_CO2 = list_zero
    else:
        list_CO2 = list_zero 
    
    if len(list_CO2) == 1:
        break

C02_rating = convert(list_CO2)

life_support = C02_rating * oxygen_rating
print(life_support)
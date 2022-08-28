with open('mynewfile1000000.txt') as f:
    lines = f.readlines()
desired_array = [int(float(numeric_string.replace(',\n',''))) for numeric_string in lines]
# desired_array  = reversed(desired_array)
# print(desired_array)
MAX = 100

for bust in desired_array:
    if bust >=MAX:
        bust = MAX-1
    
    for xx in range(bust+1):

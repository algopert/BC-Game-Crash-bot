

with open('sample5000k.txt') as f:
    lines = f.readlines()

mlist = [int((float(numeric_string.replace(',\n', ''))+0.001)*100)
         for numeric_string in lines]
# print(mlist)
cnt = len(mlist)

THRESHOLD = 160

MAX = 4
bigger2 = 0
smaller2 = 0
for i in range(MAX):
    if mlist[i] > THRESHOLD:
        bigger2 += 1

avg_max = int(1 * MAX)
avg_min = int(0.5* MAX)

print(avg_min, avg_max)

chance_cnt = 0
for i in range(cnt-MAX):
    j = i + MAX

    if (bigger2 < avg_min or bigger2> avg_max ) and mlist[j]>THRESHOLD:
        chance_cnt += 1
        
    # print(bigger2)
    if mlist[j] > THRESHOLD:
        bigger2 += 1

    if mlist[i] > THRESHOLD:
        bigger2 -= 1


# print(avg_max, avg_min)

print(f"chance  {chance_cnt}")

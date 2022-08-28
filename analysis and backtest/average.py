with open('sample5000k.txt') as f:
    lines = f.readlines()

mlist = [int((float(numeric_string.replace(',\n',''))+0.001)*100) for numeric_string in lines]
# print(mlist)
cnt = len(mlist)

MAX = 200
bigger2 = 0
smaller2 = 0
for i in range(MAX):
    if mlist[i]>199:
        bigger2 +=1
    else:
        smaller2 +=1

avg_max = 0
avg_min = 100000000000

# print(bigger2, smaller2)

for i in range(cnt-MAX):
    if bigger2>avg_max:
        avg_max = bigger2
    if bigger2<avg_min:
        avg_min = bigger2
        
    j =i + MAX
    
    if mlist[j]>199:
        bigger2 +=1
    else:
        smaller2 +=1

    if mlist[i]>199:
        bigger2 -=1
    else:
        smaller2 -=1


print(avg_max, avg_min)

print("max :  ", avg_max/MAX*100,"%")
print("min :  ", avg_min/MAX*100,"%")    
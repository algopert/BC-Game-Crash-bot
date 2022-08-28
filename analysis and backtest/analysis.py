

with open('sample5000k.txt') as f:
    lines = f.readlines()
desired_array = [int((float(numeric_string.replace(',\n',''))+0.001)*10) for numeric_string in lines]
# desired_array  = reversed(desired_array)
# print(desired_array)
MAX = 21

max_stat = [0] * MAX
max_pos = [-1] * MAX
last_pos = [0] * MAX

# print(last_pos)

pos = 0
for bust in desired_array:
    if bust >=MAX:
        bust = MAX-1
    
    for xx in range(bust+1):
        if pos - last_pos[xx]-1 > max_stat[xx]:
            max_stat[xx] = pos - last_pos[xx]-1
            max_pos[xx] = pos
    
        last_pos[xx] = pos

    pos+=1


length_tgt = [0]*MAX
for pos in range(MAX):
    length_tgt[pos] = int(max_stat[pos]*0.6)

# print("length target is : ",length_tgt)
length_tgt[20] = 7

period_min = [5000000]*MAX
period_max = [0]*MAX
start_pos = [-1]*MAX
end_pos = [-1] * MAX

bust = -1
for bust in desired_array:
    if bust >=MAX:
        bust = MAX-1
    # print(bust)
    for xx in range(bust+1):
        if start_pos[xx]>=0:
            length_cur = pos - start_pos[xx] - 1
        
            # print(length_cur)
            if length_cur> length_tgt[xx]:
                # print("------")
                if start_pos[xx]>0 and end_pos[xx]>0 and period_min[xx]> start_pos[xx]- end_pos[xx]:
                    period_min[xx] = start_pos[xx]- end_pos[xx]
                
                if start_pos[xx]>0 and end_pos[xx]>0 and period_max[xx]< start_pos[xx]- end_pos[xx]:
                    period_max[xx] = start_pos[xx]- end_pos[xx]
                
                end_pos[xx] = pos
    
        start_pos[xx] = pos

    pos+=1

print(period_min)
for pos in range(MAX):
    print(pos, max_stat[pos], length_tgt[pos], period_min[pos], period_max[pos])
# print(last_pos)
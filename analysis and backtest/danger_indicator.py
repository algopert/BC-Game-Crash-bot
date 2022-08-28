with open('sample5000k.txt') as f:
    lines = f.readlines()

THRESHOLD = 160

mlist = [int((float(numeric_string.replace(',\n', ''))+0.001)*100)
         > THRESHOLD for numeric_string in lines]

for dig in mlist:
    if dig > THRESHOLD:
        dig = 1
    else:
        dig = 0

LIMIT_LEN = 2

DANGER_LEN = 4

start_pos = -1
pos = 0
danger_max = 0
danger_min = 1000000000000
for bust in mlist:
    if bust >0:
        if start_pos>=0:
            length_cur = pos - start_pos-1
        
            # print(length_cur)
            if length_cur>= LIMIT_LEN and start_pos>=DANGER_LEN:
                # print("----",start_pos+1, pos+1, length_cur)
                s = 0
                
                for i in range(DANGER_LEN):
                    s += mlist[start_pos-i]
                if s>danger_max:
                    danger_max = s
                if s<danger_min:
                    danger_min = s

                # print("sum :", s)

        start_pos = pos

    pos+=1

print(danger_min/DANGER_LEN*100,"%   ", danger_max/DANGER_LEN*100, "%")
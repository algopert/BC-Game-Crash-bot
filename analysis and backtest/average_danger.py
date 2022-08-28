
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

THRESHOLD = 160

with open('sample5000k.txt') as f:
    lines = f.readlines()
import matplotlib.pyplot as plt


mlist = [int((float(numeric_string.replace(',\n', ''))+0.001)*100)
         for numeric_string in lines]
# print(mlist)
cnt = len(mlist)


def calc_average(avr_len):
    global mlist
    global cnt
    global THRESHOLD
    bigger2 = 0
    smaller2 = 0
    for i in range(avr_len):
        if mlist[i] > THRESHOLD:
            bigger2 += 1
        else:
            smaller2 += 1

    avg_max = 0
    avg_min = 100000000000

    # print(bigger2, smaller2)

    for i in range(cnt-avr_len):
        if bigger2 > avg_max:
            avg_max = bigger2
        if bigger2 < avg_min:
            avg_min = bigger2

        j = i + avr_len

        if mlist[j] > THRESHOLD:
            bigger2 += 1
        else:
            smaller2 += 1

        if mlist[i] > THRESHOLD:
            bigger2 -= 1
        else:
            smaller2 -= 1

    print("min :  ", avg_min/avr_len*100, "%    ",
          "max :  ", avg_max/avr_len*100, "%")

    return round(avg_min/avr_len*100, 2), round(avg_max/avr_len*100, 2)


def calc_danger_percent(danger_length, limit_len):
    # print(danger_length)
    global mlist
    global THRESHOLD
    start_pos = -1
    pos = 0
    danger_max = 0
    danger_min = 1000000000000
    for bust in mlist:
        if bust > THRESHOLD:
            if start_pos >= 0:
                length_cur = pos - start_pos-1

                # print(length_cur)
                if length_cur >= limit_len and start_pos >= danger_length:
                    # print("----",start_pos+1, pos+1, length_cur)
                    s = 0

                    for i in range(danger_length):
                        s += (mlist[start_pos-i-1] > THRESHOLD)
                    # print("++++++++++++", s)
                    if s > danger_max:
                        danger_max = s
                    if s < danger_min:
                        danger_min = s

                    # print("sum :", s)

            start_pos = pos

        pos += 1

    print(danger_min/danger_length*100, "%   ",
          danger_max/danger_length*100, "%")

    return round(danger_min/danger_length*100, 2), round(danger_max/danger_length*100, 2)


xx = []
yy = []
zz = []


len_list = [*range(3, 10, 1)]
optx = 0
opty = 0
optz = 0
opt_distribute = []

for limit_len in range(2, 5):
    max_chance_gap = 0

    for danger_len in len_list:
        # print("---------", danger_len, "------------")
        min1, max1 = calc_average(danger_len)
        min2, max2 = calc_danger_percent(danger_len, limit_len)
        y_chance = min2-min1+max1-max2
        if y_chance > max_chance_gap:
            max_chance_gap = y_chance

            optx = limit_len
            opty = danger_len
            optz = y_chance

            opt_distribute = []
            opt_distribute.append(min1)
            opt_distribute.append(min2)
            opt_distribute.append(max2)
            opt_distribute.append(max1)

        xx.append(limit_len)
        yy.append(danger_len)
        zz.append(y_chance)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
scat = ax.scatter(xx, yy, zz)

print(f"\ndanger length = {optx},  average length = {opty}: max chance gap is {max_chance_gap}\n detail values are {opt_distribute}\n")

plt.show()

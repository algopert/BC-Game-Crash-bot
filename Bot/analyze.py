def bigger(x):
    if x>199:
        return 1
    return 0


with open("./backtest_data/input.csv", 'r') as f:
    _series = f.readlines()
    f.close()


_series = list(map(int, _series))
_series = list(map(bigger, _series))



cnt = [0] * 200

_len =  len(_series)

temp = 0
for i in range(_len):
    if _series[i]==0:
        temp +=1
    else:
        cnt[temp] +=1
        temp = 0
# print(cnt)
# print(_series[0])
# print(int(_series[0]))

for i in range(20):
    print (i, " - >", cnt[i])
    
# cnt_zero = 0
# cnt_one = 0
# for i in range(_len):
#     if _series[i]==0:
#         cnt_zero += 1
        
#         if cnt_one!=0:
#             print(f', <{cnt_one}>')
#             cnt_one = 0
#     else:
#         cnt_one +=1
#         if cnt_zero!=0:
#             print(f', _{cnt_zero}_')
#             cnt_zero = 0
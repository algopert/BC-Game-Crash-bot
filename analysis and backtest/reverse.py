with open('mynewfile5000000.txt') as f:
    lines = f.readlines()
lines.reverse()
with open('sample5000k.txt', 'w') as f:
    for line in lines:
        f.write(line)
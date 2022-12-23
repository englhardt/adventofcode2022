data = [0, 1] + [int(x) if x[-1].isdigit() else 0 for x in open("input.txt").read().split()]
p1, p2 = 0, ''
for i in range(1, len(data)):
    data[i] += data[i - 1]
    p1 += i * data[i] if i % 40 == 20 else 0
    p2 += '#' if abs((i-1) % 40 - data[i]) < 2 else '\n' if i % 40 == 0 else ' '
print(p1)
print(p2)
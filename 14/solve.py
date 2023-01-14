data = open("input.txt").read().splitlines()
data = [[list(map(int, x.split(','))) for x in l.split(' -> ')] for l in data]
r = set()
for l in data:
    for (x1, y1), (x2, y2) in zip(l, l[1:]):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                r.add(x + 1j * y)
abyss = max(int(x.imag) for x in r) + 1
for x in range(0, 1000):
    r.add(x + (abyss + 1) * 1j)

num_sand_placed, foundP1 = 0, False
while 500 not in r:
    p = 500
    while True:
        if p.imag >= abyss and not foundP1:
            print(num_sand_placed)
            foundP1 = True
        if p + 1j not in r:
            p += 1j
        elif p - 1 + 1j not in r:
            p += -1 + 1j
        elif p + 1 + 1j not in r:
            p += 1 + 1j
        else:
            r.add(p)
            num_sand_placed += 1
            break
print(num_sand_placed)
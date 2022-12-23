from math import copysign

def move_closer(x, y, i, j):
    if abs(x - i) <= 1 and abs(y - j) <= 1:
        return (x, y)
    dx = i - x
    dy = j - y
    if abs(dx) >= 1 and abs(dy) >= 1:
        return (x + int(copysign(1, dx)), y + int(copysign(1, dy)))
    elif abs(dx) > 1:
        return (x + int(copysign(1, dx)), y)
    elif abs(dy) > 1:
        return (x, y + int(copysign(1, dy)))
    return (x, y)

dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

data = [(l[0], int(l[2:])) for l in open("input.txt").read().splitlines()]
rope  = [(0, 0)] * 10
seen = [set([x]) for x in rope]
for d, n in data:
    for _ in range(n):
        rope[0] = (rope[0][0] + dirs[d][0], rope[0][1] + dirs[d][1])
        seen[0].add(rope[0])
        for i in range(1, 10):
            rope[i] = move_closer(rope[i][0], rope[i][1], rope[i-1][0], rope[i-1][1])
            seen[i].add(rope[i])

print(len(seen[1]))
print(len(seen[-1]))
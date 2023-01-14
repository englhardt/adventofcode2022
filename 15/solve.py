import parse
import z3

data = list(parse.findall('x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}', open("input.txt").read()))
mhd = lambda sx, sy, bx, by: abs(sx - bx) + abs(sy - by)
covered = set([(a, b) for a, b, _, _ in data] + [(a, b) for _, _, a, b in data])
pos = set()
y = 2000000
for sx, sy, bx, by in data:
    d = mhd(sx, sy, bx, by)
    l = len(pos)
    for ox in range(sx - d + abs(sy - y), sx + d - abs(sy - y) + 1):
        pos.add((ox, y))
print(len(pos - covered))

s = z3.Solver()
x, y = z3.Int("x"), z3.Int("y")
s.add(0 <= x)
s.add(0 <= y)
s.add(x <= 4000000)
s.add(y <= 4000000)

z3_abs = lambda x: z3.If(x >= 0, x, -x)
for sx, sy, bx, by in data:
    d = abs(sx - bx) + abs(sy - by)
    s.add(z3_abs(sx - x) + z3_abs(sy - y) > d)
s.check()
m = s.model()
print(m[x].as_long() * 4000000 + m[y].as_long())
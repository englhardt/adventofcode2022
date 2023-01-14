from functools import cmp_to_key

def compare(x, y):
    if type(x) == int and type(y) == int:
        return y - x
    xl = [x] if type(x) != list else x
    yl = [y] if type(y) != list else y
    for x, y in zip(xl, yl):
        if (comp := compare(x, y)) != 0:
            return comp
    return len(yl) - len(xl)

data = open("input.txt").read().splitlines()
print(sum(idx + 1 for idx, (x, y) in enumerate(zip(data[::3], data[1::3])) if compare(eval(x), eval(y)) > 0))
p2, p6 = '[[2]]', '[[6]]'
d = sorted(map(eval, data[::3] + data[1::3] + [p2, p6]), key=cmp_to_key(compare), reverse=True)
print((d.index(eval(p2)) + 1) * (d.index(eval(p6)) + 1))
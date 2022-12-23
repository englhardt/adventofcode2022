from collections import defaultdict
from operator import itemgetter

data = open("input.txt").read().splitlines()
fs = defaultdict(list)
cur, i = ' ', 0
while i < len(data):
    w = data[i].split()
    match w[1]:
        case 'cd':
            match w[2]:
                case '/':
                    cur = ' '
                case '..':
                    cur = '/'.join(cur.split('/')[:-1])
                case _:
                    cur = f"{cur}/{w[2]}"
        case 'ls':
            while i < len(data) - 1 and data[i + 1][0] != '$':
                i += 1
                ls = data[i].split()
                new_file = f"{cur}/{ls[1]}"
                if ls[0] == 'dir':
                    fs[cur].append((new_file, 0))
                else:
                    fs[cur].append((new_file, int(ls[0])))
    i += 1

dir_sizes = {}
# Iterate upwards from deepest dirs
for d, _ in sorted([(x, len(x.split('/'))) for x in fs.keys()], key=itemgetter(1), reverse=True):
    dir_sizes[d] = sum(x[1] if x[1] > 0 else dir_sizes[x[0]] for x in fs[d])
print(sum(x for x in dir_sizes.values() if x < 100000))

to_free = 30000000 - (70000000 - dir_sizes[' '])
print(sorted(x for x in dir_sizes.values() if x >= to_free)[0])
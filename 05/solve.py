def parse_stacks(data):
    stacks = [[] for _ in range(10)]
    for l in data[7::-1]:
        for c in range(1, 34, 4):
            if l[c] != ' ':
                stacks[((c - 1) // 4) + 1].append(l[c])
    return stacks

data = open("input.txt").read().splitlines()

stacks = parse_stacks(data)
for l in data[10:]:
    num, a, b = [int(s) for s in l.split() if s.isdigit()]
    for _ in range(num):
        stacks[b].append(stacks[a].pop())
print(''.join(x[-1] for x in stacks[1:]))

stacks = parse_stacks(data)
for l in data[10:]:
    num, a, b = [int(s) for s in l.split() if s.isdigit()]
    stacks[b] += stacks[a][-num:]
    stacks[a] = stacks[a][:-num]
print(''.join(x[-1] for x in stacks[1:]))
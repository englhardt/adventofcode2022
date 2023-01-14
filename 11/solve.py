from functools import reduce
from operator import mul

data = open("input.txt").read().splitlines()
num_monkeys = (len(data) + 1) // 7
monkey_items = [[] for _ in range(num_monkeys)]
monkey_op = [''] * num_monkeys
monkey_div = [0] * num_monkeys
monkey_targets = [[0, 0] for _ in range(num_monkeys)]
monkey_inspections = [0] * num_monkeys

i = 0
while i < len(monkey_items):
    monkey_items[i] = [int(x) for x in data[i * 7 + 1][18:].split(', ')]
    monkey_op[i] = data[i * 7 + 2][19:]
    monkey_div[i] = int(data[i * 7 + 3][21:])
    monkey_targets[i][0] = int(data[i * 7 + 4][29:])
    monkey_targets[i][1] = int(data[i * 7 + 5][29:])
    i += 1
lcm_mod = reduce(mul, monkey_div)

def sim(monkey_items, num_rounds, part_div):
    for i in range(num_rounds):
        for m in range(num_monkeys):
            monkey_inspections[m] += len(monkey_items[m])
            for old in monkey_items[m]:
                new = eval(monkey_op[m]) // part_div % lcm_mod
                if new % monkey_div[m] == 0:
                    monkey_items[monkey_targets[m][0]].append(new)
                else:
                    monkey_items[monkey_targets[m][1]].append(new)
            monkey_items[m] = []
    return reduce(mul, sorted(monkey_inspections)[-2:])

print(sim([x[:] for x in monkey_items], 20, 3))
print(sim(monkey_items, 10_000, 1))
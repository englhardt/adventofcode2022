data = open("input.txt").read().splitlines()
deers, acc = [], 0
for v in data:
    if not v:
        deers.append(acc)
        acc = 0
    else:
        acc += int(v)
print(max(deers))
print(sum(sorted(deers)[-3:]))
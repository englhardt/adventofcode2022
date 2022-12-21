def getPriority(x):
    return ord(x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27

data = open("input.txt").read().splitlines()
accP1 = 0
for d in data:
    mid = len(d) // 2
    overlap = set(d[:mid]) & set(d[mid:])
    accP1 += getPriority(next(iter(overlap)))
print(accP1)

accP2 = 0
for i in range(len(data))[::3]:
    overlap = set(data[i]) & set(data[i + 1]) & set(data[i + 2])
    accP2 += getPriority(next(iter(overlap)))
print(accP2)
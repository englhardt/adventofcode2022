data = [[int(x) for x in l] for l in open("input.txt").read().splitlines()]
n = len(data)
visible = n * 4 - 4
for i in range(1, n - 1):
    for j in range(1, n - 1):
        cur = data[i][j]
        visible += int(all(x < cur for x in data[i][0:j]) \
            or all(x < cur for x in data[i][j+1:])
            or all(x[j] < cur for x in data[0:i]) \
            or all(x[j] < cur for x in data[i+1:]))
print(visible)

def score(tree, view):
    s = 0
    for v in view:
        s += 1
        if v >= tree:
            break
    return s

best = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        cur = data[i][j]
        cur_score = score(cur, data[i][j-1::-1]) \
            * score(cur, data[i][j+1:]) \
            * score(cur, [x[j] for x in data[i+1:]]) \
            * score(cur, [x[j] for x in data[i-1::-1]])
        best = max(best, cur_score)
print(best)
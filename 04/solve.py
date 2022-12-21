range_subset = lambda r1, r2: r1.start in r2 and (len(r1) == 0 or r1[-1] in r2)
check_subset = lambda r1, r2: range_subset(r1, r2) or range_subset(r2, r1)
range_overlap = lambda r1, r2: r1.start <= r1.start <= r2[-1] and r2.start <= r1[-1]
check_overlap = lambda r1, r2: range_overlap(r1, r2) or range_overlap(r2, r1)

def parse_range(s):
    low, high = map(int, s.split('-'))
    return range(low, high + 1)

data = open("input.txt").read().splitlines()
ranges = []
for s in data:
    s1, s2 = s.split(',')
    ranges.append((parse_range(s1), parse_range(s2)))
print(sum(map(lambda r: check_subset(r[0], r[1]), ranges)))
print(sum(map(lambda r: check_overlap(r[0], r[1]), ranges)))
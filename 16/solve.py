from collections import defaultdict
from functools import cache


raw = open("input.txt").read().splitlines()
data = []
valves, flows, dist = set(), {}, defaultdict(lambda: 100)
for r in raw:
    s = r.split()
    valve = s[1]
    valves.add(valve)
    if f := int(s[4][5:-1]):
        flows[valve] = f
    for other in [x.replace(',', '') for x in s[9:]]:
        dist[valve, other] = 1

# Floyd–Warshall algorithm
for k in valves:
    for i in valves:
        for j in valves:
            dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])

# dynamic programming top down with caching
@cache
def sim(t, v, closed, p2=False):
    return max([flows[o] * (t - dist[v, o] - 1) + sim(t - 1 - dist[v, o], o, closed - {o}, p2)
               for o in closed if dist[v, o] < t - 1] + [sim(26, 'AA', closed) if p2 else 0])

print(sim(30, 'AA', frozenset(flows)))
print(sim(26, 'AA', frozenset(flows), True))
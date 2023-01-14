from collections import defaultdict, deque
data = open("input.txt").read().splitlines()
n, m = len(data), len(data[0])
heights = defaultdict(int)
start, end = 0, 0
for y in range(n):
    for x in range(m):
        match data[y][x]:
            case 'S':
                start = (x, y)
                heights[(x, y)] = 0
            case 'E':
                end = (x, y)
                heights[(x, y)] = ord('z') - ord('a')
            case c:
                heights[(x, y)] = ord(c) - ord('a')
  
def get_neighbors(pos):
    x, y = pos
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            other = (x + dx, y + dy)
            if 0 <= other[0] < m \
                and 0 <= other[1] < n \
                and heights[other] - heights[pos] <= 1:
                yield other

def bfs(start):
    queue, visited = deque([(start, 0)]), set()
    max_height = 0
    while queue:
        p, steps = queue.popleft()
        max_height = max(max_height, heights[p])
        if p == end:
            return steps
        if p not in visited:
            for other in get_neighbors(p):
                if other not in visited:
                    queue.append((other,  steps + 1))
            visited.add(p)
    return float("inf")
print(bfs(start))
print(min(bfs(p) for p, h in heights.items() if h == 0))
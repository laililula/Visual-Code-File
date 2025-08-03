import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start, visited):
    print(start, end=' ')
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        cur = queue.popleft()
        print(cur, end=' ')
        for neighbor in graph[cur]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

n, m , k = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    add_edge(graph, u, v)
for i in graph.keys():
    graph[i].sort()
dfs(graph, k, set())
print('')
bfs(graph, k)
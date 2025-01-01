import math
from queue import PriorityQueue


def Network(graph,source):
    
    visited = [False] * len(graph)
    distance = [-math.inf] * len(graph)
    distance[source] = math.inf
    pq = PriorityQueue()
    pq.put((-1 * distance[source], source))
    while pq.empty() == False:
        u = pq.get()[1]
        if u in visited:
            continue
        visited[u] = True
        for v in graph[u]:
            temp = min(distance[u], v[1])
            if(temp > distance[v[0]]):
                distance[v[0]] = temp
                pq.put((-1 * distance[v[0]], v[0]))
    for x in range(len(distance)):
        if(distance[x] == -math.inf):
            distance[x] = -1
        if(distance[x] == math.inf):
            distance[x] = 0
    data2.write(f"{str(distance[1:])} \n")
data1 = open("input5.txt", "r")
data2 = open("output5.txt", "w")
for item in range(int(data1.readline())):
    x,y = map(int, data1.readline().split())
    graph = [[] for x in range(x + 1)]
    for j in range(y):
        a,b,c = map(int, data1.readline().split())
        graph[a].append((b,c))
    source = int(data1.readline())
    Network(graph, source)
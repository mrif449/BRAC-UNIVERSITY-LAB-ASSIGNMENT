import math
from queue import PriorityQueue

def Dijkstra(Graph,source):
    visited = [False]*len(Graph)
    distance = [math.inf]*len(Graph)
    distance[source] = 0
    pq = PriorityQueue()
    pq.put((distance[source], source))
    while pq.empty() == False:
        u = pq.get()[1]
        if u in visited:
            continue
        visited[u] = True
        for v in Graph[u]:
            temp = distance[u] + v[1]
            if temp < distance[v[0]]:
                distance[v[0]] = temp
                pq.put((distance[v[0]],v[0]))
    data2.write(f"{str(distance[len(Graph)-1])} \n")

data1 = open("input1.txt","r")
data2 = open("output1.txt","w")
source = 1
for a in range(int(data1.readline())):
    x,y = map(int, data1.readline().split())
    Graph = [[] for i in range(x + 1)]
    for j in range(y):
        a,b,c = map(int, data1.readline().split())
        Graph[a].append((b,c))
    Dijkstra(Graph, source)
data2.close()
import math
from queue import PriorityQueue

def Dijkstra(Graph,source):
    pq = PriorityQueue()
    visited = [False] * len(Graph)
    distance = [math.inf] * len(Graph)
    prev = [-1] * len(Graph)
    distance[source] = 0
    pq.put((distance[source], source))
    while pq.empty() == False:
        u = pq.get()[1]
        if u in visited:
            continue
        visited[u] = True

        for v in Graph[u]:
            temp = distance[u] + v[1]
            if(temp < distance[v[0]]):
                distance[v[0]] = temp
                prev[v[0]] = u
                pq.put((distance[v[0]], v[0]))

    counter = len(Graph)-1
    way = []
    while(counter != 1):
        way.append(counter)
        counter = prev[counter]
    way.append(1)
    way.reverse()
    data2.write(str(way) + "\n")


data1 = open("input2.txt","r")
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
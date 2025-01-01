import queue as q
def BFS(visited, graph, node, endPoint):
    output = open("output2.txt","w")
    visited.append(node)
    q.append(node)
    while q:
        pops = q.pop(0)
        store = (pops) + " "
        output.write(store)
        if pops == endPoint:
            break
        for x in graph[pops]:
            if x not in visited:
                visited.append(x)
                q.append(x)

data = open("input1.txt","r")
PlaceCount = int(data.readline())
graph = {}
for y in range(PlaceCount):
    elements = list(map(str,data.readline().split()))
    graph.update({elements[0]:elements[1:len(elements)]})
visited = []
q = []
BFS(visited, graph, '1', '12')
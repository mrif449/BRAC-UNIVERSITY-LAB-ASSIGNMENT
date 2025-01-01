def DFS_VISIT(graph,node):
    global printed
    global visited
    if node not in printed:
        printed.append(node)
        for x in graph[node]:
            if x not in visited:
                DFS_VISIT(graph,x)

def DFS(graph,endPoint):
    output = open("output3.txt","w")
    output.write("Places: ")
    for y in graph:
        if y not in visited:
            DFS_VISIT(graph,y)
    for z in printed:
        output.write(f"{z} ")
        if z == endPoint:
            break
        
printed = []
visited = []
data = open("input1.txt","r")
PlaceCount = int(data.readline())
graph = {}
for y in range(PlaceCount):
    elements = list(map(str,data.readline().split()))
    graph.update({elements[0]:elements[1:len(elements)]})
DFS(graph,"12")
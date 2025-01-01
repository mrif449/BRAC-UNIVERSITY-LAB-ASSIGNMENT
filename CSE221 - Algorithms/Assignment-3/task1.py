def GraphBuiling(data):
    graph = open("output1.txt","w")
    dictionary = {}
    for x in range(PlaceCount):
        elements = list(map(int,data.readline().split()))
        dictionary.update({elements[0]:elements[1:len(elements)]})
    for k,v in dictionary.items():
        output = str(k) + " --> " + str(v)
        graph.write(f"{output}\n")
data = open("input1.txt","r")
PlaceCount = int(data.readline())
GraphBuiling(data)
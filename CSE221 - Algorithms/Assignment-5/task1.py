def Assignment_Selection(array,n):
    taken = []
    start = 0
    taken.append(array[0])
    for x in range(1,n):
        if array[x][0] >= array[start][1]:
            taken.append(array[x])
            start = x
    data2.write(str(len(taken))+"\n")
    for y in taken:
        data2.write(f"{y[0]} {y[1]}\n")
    
data1 = open("input1.txt","r")
data2 = open("output1.txt","w")
array = []
data = []
text = data1.readlines()
counter = int(text[0])
time = [[0,0]]*counter
for x in text:
    array.append(x)
for y in array:
    data.append(y[:-1])
for z in range(counter):
    for a in data:
        a.split()
n = int(data[0] )
data.pop(0)
start = 0
final = []
for x in range(len(data)):
    val = data[x].split()
    temp = []
    temp.append(int(val[0]))
    temp.append(int(val[1]))
    final.append(temp)
final.sort(key=lambda x: x[1])


Assignment_Selection(final,n)
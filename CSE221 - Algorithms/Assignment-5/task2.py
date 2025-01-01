def Schedule_Intervals(array,n):
        global taken
        start = 0
        taken.append(array[0])
        for x in range(1,len(array)):
            if array[x][0] >= array[start][1]:
                taken.append(array[x])
                start = x
data1 = open("input2.txt","r")
data2 = open("output2.txt","w")
array = []
data = []
datas = []
taken = []
n = int(data1.readline(1))
m = int(data1.readline(2)[::-1])
data = data1.readlines()
for x in range(1,n+1):
    array.append(data[x])
for y in array:
    y = y[:-1]
    datas.append(y)
start = 0
final = []
for x in range(len(datas)):
    val = datas[x].split()
    temp = []
    temp.append(int(val[0]))
    temp.append(int(val[1]))
    final.append(temp)
final.sort(key=lambda x: x[1])


for z in range(m):
    trys = []
    for y in final:
        if y not in taken:
            trys.append(y) 
    Schedule_Intervals(trys,n)
data2.write(str(len(taken)))
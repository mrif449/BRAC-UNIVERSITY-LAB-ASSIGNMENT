import math
data1 = open("input4.txt","r")
data2 = open("output4.txt","w")
datas =data1.readlines()
array = []
for x in datas:
    temp = x.split()
    temp2 = []
    temp2.append(int(temp[0]))
    temp2.append(int(temp[1]))
    array.append(temp2)
array.pop(len(array)-1)
for y in range(len(array)):
    counter = 0
    for z in range(array[y][0],array[y][1]+1):
        if math.sqrt(z) == math.sqrt(z)//1:
            counter += 1
    data2.write(str(counter)+"\n")
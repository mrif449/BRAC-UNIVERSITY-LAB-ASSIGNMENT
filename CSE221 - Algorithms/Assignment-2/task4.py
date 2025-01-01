def MERGE(array):
    if len(array) > 1:
        right = len(array)//2
        left = array[:right]
        mid = array[right:]
        MERGE(left)
        MERGE(mid)
        x = 0
        y = 0 
        z = 0
        while x < len(left) and y < len(mid):
            if left[x] < mid[y]:
                array[z] = left[x]
                x += 1
            else:
                array[z] = mid[y]
                y += 1
            z += 1
        while x < len(left):
            array[z] = left[x]
            x += 1
            z += 1

        while y < len(mid):
            array[z] = mid[y]
            y += 1
            z += 1


data = open("input4.txt","r")
array = []
for x in data:
    array.append(x)
element = array[1].split()
array2 = []
for y in element:
    array2.append(int(y))

MERGE(array2)
data2 = open("output4.txt","w")
for a in array2:
    data2.write(str(a)+" ")
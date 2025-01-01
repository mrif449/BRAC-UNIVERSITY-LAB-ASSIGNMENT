def bubbleSort(arr):
    counter = 0
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t
                counter += 1
        if i > 0 and counter == 0:
            break
    data2 = open("output1.txt","w")
    for a in arr:
        data2.write(str(a)+" ")

data = open("input1.txt","r")
array = []
for x in data:
    array.append(x)
element = array[1].split()
array2 = []
for y in element:
    array2.append(int(y))

bubbleSort(array2)
data.close()
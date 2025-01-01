def selectionSort(arr,lens):
    length = len(arr)
    for x in range(length):
        initial = x
        for y in range(x + 1, length):
            if arr[y] < arr[initial]:
                initial = y
        arr[x], arr[initial] = arr[initial], arr[x]

    data2 = open("output2.txt","w")
    for a in range(lens):
        data2.write(str(arr[a]) + " ")

data = open("input2.txt","r")
array = []
for x in data:
    array.append(x)
element = array[1].split()
array2 = []
for y in element:
    array2.append(int(y))

size = len(array2)

temp = (array[0]).split()
lens = int(temp[1])

selectionSort(array2,lens)
data.close()
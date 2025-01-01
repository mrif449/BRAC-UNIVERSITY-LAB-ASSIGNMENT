def insertionSort(arr,arr2):
    new = []
    for a in arr2:
        new.append(a)
    for x in range(1, len(arr2)):
        key = arr2[x]
        j = x-1
        while j >= 0 and key > arr2[j]:
            arr2[j+1] = arr2[j]

            j = j - 1
            new.append(j)
        arr2[j+1] = key
    check = []
    check2 = []
    end = 0
    for a in range(len(arr2)):
        for b in range(len(arr2)):
            if arr2[a] == new[b]:
                check.append(b)
    for p in check:
        if p not in check2:
            check2.append(p)
    data2 = open("output3.txt", "w")
    for a in check2:
        data2.write(str(arr[a]) + " ")
data = open("input3.txt","r")
array = []
for x in data:
    array.append(x)
element = array[1].split()
element2 = array[2].split()
array2 = []
for y in element:
    array2.append(int(y))
array3 = []
for z in element2:
    array3.append(int(z))
insertionSort(array2,array3)
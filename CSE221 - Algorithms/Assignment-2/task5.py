# Answer of 5(a)

def PARTITION(a, p, r):
  pivot = a[r]
  x = p - 1
  for y in range(p, r):
    if a[y] <= pivot:
      x = x + 1
      (a[x], a[y]) = (a[y], a[x])
  (a[x + 1], a[r]) = (a[r], a[x + 1])
  return x + 1


def QUICKSORT(array, p, q):
  if p < q:
    pi = PARTITION(array, p, q)
    QUICKSORT(array, p, pi - 1)
    QUICKSORT(array, pi + 1, q)


data = open("input5.txt","r")
data = data.read()
data = data.split()
array1 = []
array2 = []
array3 = []
for x in data:
    array1.append(x)

for y in range(len(array1)):
    if y <= 1:
        continue
    elif array1[y] == "K=":
        break
    else:
        array2.append(int(array1[y]))

for z in range(len(array1)):
    if array1[z] == "K=":
        array3.append(int(array1[z+1]))

size = len(array2)

QUICKSORT(array2, 0, len(array2) - 1)
data2 = open("output5a.txt","w")
for a in array2:
    data2.write(f"{str(a)} ")



# Answer of 5(b)

def partition(array, l, r, idx):
  pivot = array[idx]
  right=[] 
  left=[] 
  for x in range(l, r+1): 
    if x==idx: 
      pass
    elif array[x] <= pivot:
      left.append(array[x])
    else:
      right.append(array[x])
  endL = len(left) + l
  array[l: endL] = left 
  array[endL] = pivot
  array[endL+1:r+1] = right
  return endL

def findK(array, l, r, k):
  if l <= r:
    idx = l
    pivotP = partition(array,l, r,  idx)
    if pivotP==k:
      return array[k]
    elif pivotP < k:
        return findK(array,pivotP+1, r, k)
    else:
        return findK(array, l, pivotP-1, k)

data = open("input5.txt","r")
data = data.read()
data = data.split()
array1 = []
array2 = []
array3 = []
for x in data:
    array1.append(x)

for y in range(len(array1)):
    if y <= 1:
        continue
    elif array1[y] == "K=":
        break
    else:
        array2.append(int(array1[y]))

for z in range(len(array1)):
    if array1[z] == "K=":
        array3.append(int(array1[z+1]))

data2 = open("output5b.txt","w")
for x in array3:
  kth_smallest = findK(array2, 0, len(array2)-1, x-1)
  
  data2.write(str(f"{kth_smallest}\n"))
data = open("input4.txt","r")
data =  data.read()
array = []
for x in data:
    array.append(x)

n = int(array[0])
array1 = []
array2 = []
array = array[2:]
for a in array:
    if a == " ":
        array.remove(a)
temp = []
for z in range((n*n)+n):
    if array[z] != "\n":
        temp.append(int(array[z]))
    else:
        array1.append(temp)
        temp = []
temp2 = []
array = array[(n*n)+n:]
for b in array:
    if b != "\n":
        temp2.append(int(b))
    else:
        array2.append(temp2)
        temp2 = []

def Multiply_matrix(A,B):
    global n
    C = [[0]*n]*n
    final = []
    for i in range(n):
        for j in range(n):
                C[i][j]=0
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
                final.append(C[i][j])
    out = open("output4.txt","w")
    for l in range(len(final)):
        out.write(f'{final[l]} ')
        if (l+1) % n == 0:
            out.write("\n")
Multiply_matrix(array1,array2)


#Explanation
"""
We mainly get the time complexity by counting the number of loops. Here in the function 3 for loops are used for the calculation. So the time complexity is n^3
"""
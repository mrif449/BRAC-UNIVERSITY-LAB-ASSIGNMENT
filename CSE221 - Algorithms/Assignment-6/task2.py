data1 = open("input2.txt","r")
data2 = open("output2.txt","w")
def LCS(X, Y):
    m = len(X)+1
    n = len(Y)+1
    array = [[0]*m]*n
    result = ""
    #array = [[0 for x in range(n+1)] for x in range(m+1)]
    data = ["Yasnaya","Rozhok","School","Pochinki","Farm","Mylta","Shelter","Prison"]
    for x in range(m):
        for y in range(n):
            if x == 0 or y == 0:
                array[x][y] = 0
            elif string1[x-1] == string2[y-1]:
                array[x][y] = array[x-1][y-1] + 1
            else:
                array[x][y] = max(array[x-1][y], array[x][y-1])

    idx = array[m-1][n-1]

    LCS = [""] * (idx+1)
    LCS[idx] = ""

    x = m-1
    y = n-1
    while x > 0 and y > 0:

        if string1[x-1] == string2[y-1]:
            LCS[idx-1] = string1[x-1]
            x -= 1
            y -= 1
            idx -= 1

        elif array[x-1][y] > array[x][y-1]:
            x -= 1
        else:
            y -= 1
            
    for z in LCS:
        if z == "Y":
            result += data[0]+" "
        elif z == "R":
            result += data[1]+" "
        elif z == "S":
            result += data[2]+" "
        elif z == "P":
            result += data[3]+" "
        elif z == "F":
            result += data[4]+" "
        elif z == "M":
            result += data[5]+" "
        elif z == "H":
            result += data[6]+" "
        elif z == "I":
            result += data[7]+" "
        else:
            pass
    data2.write(result)
    total = len(string1)
    counter = 0
    for a in range(len(string1)):
        if string1[a] == string2[a]:
            counter += 1
    answer = int((counter/total)*100)
    data2.write(f"\nCorrectness of prediction: {str(answer)}%")
steps = data1.readline()
string1 = data1.readline()
string1 = string1[:-1]
string2 = data1.readline()
LCS(string1,string2)
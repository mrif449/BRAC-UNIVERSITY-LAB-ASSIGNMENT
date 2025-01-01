def LCS(X,Y,Z):
    m = len(X)+1
    n = len(Y)+1
    o = len(Z)+1
    array = [[[0 for i in range(o)] for j in range(n)]for k in range(m)]
    for i in range(m): 
        for j in range(n): 
            for k in range(o): 
                if (i == 0 or j == 0 or k == 0): 
                    array[i][j][k] = 0
                      
                elif (X[i-1] == Y[j-1] and
                      X[i-1] == Z[k-1]): 
                    array[i][j][k] = array[i-1][j-1][k-1] + 1
  
                else: 
                    array[i][j][k] = max(max(array[i-1][j][k], array[i][j-1][k]), array[i][j][k-1]) 
  
    data2.write(str(array[m-1][n-1][o-1]))
    


data1 = open("input3.txt","r")
data2 = open("output3.txt","w")
string1 = data1.readline()
string2 = data1.readline()
string3 = data1.readline()
string1 = (string1[:-1])
string2 = (string2[:-1])
LCS(string1,string2,string3)

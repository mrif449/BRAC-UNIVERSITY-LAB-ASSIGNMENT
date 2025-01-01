data = open("input.txt","r")
data = data.read()
array1 = []
array2 = []
array3 = []
file = data.split("\n")
for x in file:
  array1.append(x)
total_number = 0
total_word = 0
odd_parity = 0
even_parity = 0
not_parity = 0
palindrome = 0
not_palindrome = 0
def parity(number):
  global total_number
  global odd_parity
  global even_parity
  global not_parity
  global array2
  total_number += 1
  if "." in number:
        not_parity += 1
        array2.append(f"{number} cannot have parity and")
  elif int(number)%2 == 0:
        even_parity += 1 
        array2.append(f"{number} has even parity and")
  else:
        odd_parity += 1
        array2.append(f"{number} has odd parity and")
def isPalindrome(word):
    global total_word
    global array3
    global palindrome
    global not_palindrome
    total_word += 1
    pal = True
    N = len(word)
    i = 0
    if word == "":
        return False
    N = len(word)
    i = 0
    for x in range(i,N//2):
        if word[i] != word[N-1-i]:
            return False
        i += 1
    return True 
                  
for z in array1:
    var = z.split()
    parity(var[0]) 
    isPalindrome(var[1])
    if isPalindrome(var[1]) == True:
        palindrome += 1
        array3.append(f" {var[1]} is a palindorme")
    else:
        not_palindrome += 1
        array3.append(f" {var[1]} is not a palindorme")

array4 = []
for i in array3:
    if i not in array4:
        array4.append(i)

length = len(array2)
files = open("output.txt","w")
for y in range(length):
   temp = array2[y]+array4[y]+"\n"
   files.write(temp)

opp = (odd_parity/total_number)*100
epp = (even_parity/total_number)*100
npp = (not_parity/total_number)*100
pp = (palindrome/len(array4))*100
np = (not_palindrome/len(array4))*100

newf = open("record.txt","w")
newf.write(f"Percentage of odd parity: {int(opp)}%\n")
newf.write(f"Percentage of even parity: {int(epp)}%\n")
newf.write(f"Percentage of no parity: {int(npp)}%\n")
newf.write(f"Percentage of palindrome: {int(pp)}%\n")
newf.write(f"Percentage of non-palindrome: {int(np)}%")

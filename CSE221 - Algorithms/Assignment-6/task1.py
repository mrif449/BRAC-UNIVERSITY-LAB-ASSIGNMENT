data1 = open("input1.txt","r")
data2 = open("output1.txt","w")
number = int((data1.readline()))
def Minimum_Step(number):
    counter = 0
    data2.write(str(number)+"->")
    while number != 0:
        max = 0
        for x in str(number):
            if ord(x) > max:
                max = ord(x)
        number -= int(chr(max))
        if number != 0:
            data2.write(str(number) + "->")
        else:
            data2.write(str(number) + ".\n")
        counter += 1
    data2.write(str(counter))
Minimum_Step(number)
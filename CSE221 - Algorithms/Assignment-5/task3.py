def work(array,sequence):
    counter = 0
    string = ""
    array2 = []
    sum1 = 0
    sum2 = 0
    for x in sequence:
        if x == "J":
            counter += 1

    for y in sequence:
        if y == "J":
            string += str(array[0])
            array2.append(array[0])
            sum1 += array[0]
            array.pop(0)
        else:
            string += str(array2[len(array2)-1])
            sum2 += array2[len(array2)-1]
            array2.pop(len(array2)-1)
    data2.write(f"{string}\nJack will work for {sum1} hours\nJill will work for {sum2} hours")


data1 = open("input3.txt","r")
data2 = open("output3.txt","w")
time = []
duration = data1.readline()
duration2 = data1.readline()
sequence = data1.readline()
duration2.split()
for x in duration2:
    if x != " " and x != "\n":
        time.append(int(x))
time.sort()
work(time,sequence)
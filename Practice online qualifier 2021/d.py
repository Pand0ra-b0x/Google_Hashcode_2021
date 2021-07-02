import numpy as np
filename = 'd_many_pizzas.txt'
data = np.loadtxt(filename, delimiter = ',' , dtype = str)
numOfPizza, teamOf2, teamOf3, teamOf4 = data[0].split()
numOfPizza = int(numOfPizza)
teamOf2 = int(teamOf2)
teamOf3 = int(teamOf3)
teamOf4 = int(teamOf4)
data = np.delete(data, 0)
arr = []
c=0
for i in data:
    word = ""
    for j in i:
        word = word+j
    word = word + " "+str(c)
    c += 1
    arr.append(word)
arr = sorted(arr, reverse = True)
l = 0
u = 0
pizzaTeam3 = []
pizzaTeam4 = []
pizzaTeam2 = []

available_pizza = len(arr)
total_deliveries = 0
while (available_pizza > 2):
    if (available_pizza >= 3 and teamOf3 > 0):
        c = 3
        u += 3
        temp = []
        for i in range(l,u):
            c -= 1
            p = arr[i][-1]
            temp.append(p)
            if (c == 0):
                break
        teamOf3 -= 1
        l += 3
        available_pizza -= 3
        total_deliveries += 1
        pizzaTeam3.append(temp)
        temp = []

    if (available_pizza >= 4 and teamOf4 > 0):
        c = 4
        u += 4
        temp = []
        for i in range(l,u):
            c -= 1
            p = arr[i][-1]
            temp.append(p)
            if (c == 0):
                break
        teamOf4 -= 1
        l += 4
        available_pizza -=4
        total_deliveries += 1
        pizzaTeam4.append(temp)
        temp = []

    if (available_pizza >= 2 and teamOf2 > 0):
        c = 2
        u += 2
        temp = []
        for i in range(l,u):
            c -= 1
            p = arr[i][-1]
            temp.append(p)
            if (c == 0):
                break
        teamOf2 -= 1
        l += 2
        available_pizza -= 2
        total_deliveries += 1
        pizzaTeam2.append(temp)
        temp = []
    
    if (teamOf2+teamOf3+teamOf4 == 0):
        break
import sys
stdoutOrigin = sys.stdout
sys.stdout = open("ans_d.txt", "w")
print(total_deliveries)
while (total_deliveries > 0):
    
    if(len(pizzaTeam2)>0):
        line = ""
        line = " ".join([str(elm) for elm in pizzaTeam2[0]])
        pizzaTeam2.pop(0)
        print("2",line)
        total_deliveries -= 1
    
    if(len(pizzaTeam3)>0):
        line = ""
        line = " ".join([str(elm) for elm in pizzaTeam3[0]])
        pizzaTeam3.pop(0)
        print("3",line)
        total_deliveries -= 1
    
    if(len(pizzaTeam4)>0):
        line = ""
        line = " ".join([str(elm) for elm in pizzaTeam4[0]])
        pizzaTeam4.pop(0)
        print("4",line)
        total_deliveries -= 1
sys.stdout.close()
sys.stdout = stdoutOrigin
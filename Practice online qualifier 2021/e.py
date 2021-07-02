import numpy as np
filename = 'e_many_teams.txt'
data = np.loadtxt(filename, delimiter = ',' , dtype = str)
numOfPizza, teamOf2, teamOf3, teamOf4 = data[0].split()
numOfPizza = int(numOfPizza)
teamOf2 = int(teamOf2)
teamOf3 = int(teamOf3)
teamOf4 = int(teamOf4)
data = np.delete(data, 0)
t2, t3, t4 = teamOf2, teamOf3, teamOf4
l = 0
u = 0
pizzaTeam3 = []
pizzaTeam4 = []
pizzaTeam2 = []

available_pizza = len(data)
total_deliveries = 0
while (available_pizza > 2):
    if (available_pizza >= 3):
        c = 3
        u += 3
        temp = []
        for i in range(l,u):
            c -= 1
            temp.append(i)
            if (c == 0):
                break
        t3 -= 1
        l += 3
        available_pizza -= 3
        total_deliveries += 1
        pizzaTeam3.append(temp)
        temp = []

    if (available_pizza >= 4):
        c = 4
        u += 4
        temp = []
        for i in range(l,u):
            c -= 1
            temp.append(i)
            if (c == 0):
                break
        t4 -= 1
        l += 4
        available_pizza -=4
        total_deliveries += 1
        pizzaTeam4.append(temp)
        temp = []

    if (available_pizza >= 2):
        c = 2
        u += 2
        temp = []
        for i in range(l,u):
            c -= 1
            temp.append(i)
            if (c == 0):
                break
        t2 -= 1
        l += 2
        available_pizza -= 2
        total_deliveries += 1
        pizzaTeam2.append(temp)
        temp = []
import sys
stdoutOrigin = sys.stdout
sys.stdout = open("ans_e.txt", "w")
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
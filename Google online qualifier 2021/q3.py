import numpy as np
filename = 'c.txt'
data = np.loadtxt(filename, delimiter = ',' , dtype = str)
duration, nOfIntersections, nOfStreets, nOfCars, bonus = data[0].split()
duration = int(duration)
nOfIntersections = int(nOfIntersections)
nOfStreets = int(nOfStreets)
nOfCars = int(nOfCars)
bonus = int(bonus)
data = np.delete(data, 0)
streetName = []
startStreet = []
endStreet = []
timeStreet = []
for i in range(0, nOfStreets):
    start, end, name, time = data[i].split()
    endStreet.append(end)
    streetName.append(name)
    timeStreet.append(int(time))
    startStreet.append(start)
carPath = []
carData = []
for i in range(nOfStreets, (nOfStreets+nOfCars)):
    carData.append(data[i])  
for i in carData:
    p = i.split()
    temp = []
    for j in range(1, int(p[0])+1):
        d = streetName.index(p[j])
        temp.append(endStreet[d])
    carPath.append(temp)
intersections = []
for l in carPath:
    intersections += l
intersections = list(set(intersections))
intersection_road = []
for i in intersections:
    temp = []
    for j in range(len(endStreet)):
        if (endStreet[j] == i):
            temp.append(streetName[j])
    intersection_road.append(temp)
intersection_timers = []
for i in intersections:
    temp = []
    for j in range(len(startStreet)):
        if(startStreet[j] == i):
            temp.append(timeStreet[j])
    intersection_timers.append(min(temp))
import sys
stdoutOrigin = sys.stdout
sys.stdout = open("ans_c.txt", "w")
length = len(intersections)
print(length)
import math
for i in range(length):
    print(intersections[i])
    print(len(intersection_road[i]))
    for j in intersection_road[i]:
        avg = math.ceil(sum(intersection_timers)/len(intersection_timers))
        if(intersection_timers[i] == min(intersection_timers)):
            p = intersection_timers[i]
        else:
            p = avg
        print(j + ' ' + str(p))
sys.stdout.close()
sys.stdout = stdoutOrigin
import sys
import math
from random import shuffle
from draw import drawPath

cities = 0

nodeDict = {}
class Node():
    def __init__(self,index, xc, yc):
        self.i = index
        self.x = xc
        self.y = yc


def takeInput():
    global cities
    #f = open(sys.argv[1],'r').read().splitlines()

    f = open("data/a280",'r').read().splitlines()
    #tprint(f)

    cities = len(f)
    print(cities)
    for a in f:
        m = a.split()
        #print(m)
        print(m)
        i = int(m[0])
        x = float(m[1])
        y = float(m[2])
        #m = [float(y) for y in m]
        #m = [int(y) for y in m]
        #print (m[0])
        #print(m[1])
        #print(m[2])
        nodeDict[i] = Node(i, x, y)
    print(len(nodeDict))
    return

step = 0
def hillClimbOneStep(tour):
    global step
    #print(step)
    step += 1
    global cities
    possible_neighbours = get2OptNeighbours(tour)
    min_tour_length = getTourLength(tour)
    min_tour = 0
    localMinima = True 
    for x in possible_neighbours:
        if getTourLength(x) < min_tour_length:
            localMinima = False 
            min_tour = x
            min_tour_length = getTourLength(x)

    return min_tour, min_tour_length, localMinima

def hillClimbFull(initial_tour):

    global cities
    change = True
    min_tour_length = 00000000
    min_tour = 0
    tour = initial_tour
    while True:
        tour, tour_length,localMinima = hillClimbOneStep(tour)
        if localMinima == True:
            print("minimum tour found")
            break
        else:
            min_tour_length = tour_length
            min_tour = tour

    return min_tour_length, min_tour

def get2OptNeighbours(order):

    global cities
    final_neighbours = []
    for x in range(len(order)):
        for y in range(len(order)):
            if x != y:
                new_order = order[:x] + order[x:y][::-1] + order[y:]
                final_neighbours.append(new_order)
    return final_neighbours

def get3OptNeigbours(s):
    return

def getTourLength(tour):

    global cities
    if len(tour) == 0:
        return 0

    length = 0
    if len(tour) == 2:
        return getDistance(nodeDict[tour[0]],nodeDict[tour[1]])

    for x in range(len(tour)-1):
        length += getDistance(nodeDict[tour[x]],nodeDict[tour[x+1]]) 
    
    length += getDistance(nodeDict[tour[0]],nodeDict[tour[-1]])

    return length

def getDistance(n1, n2):
    return math.sqrt((n1.x-n2.x)*(n1.x-n2.x) + (n1.y-n2.y)*(n1.y-n2.y))

def getRandomTour():
    mm = [x for x in range(1,cities+1)]
    shuffle(mm)
    return mm

def NearestNeighbourTour():
    tour = []
    all_cities = [x for x in range(1, cities + 1)]
    city = all_cities[0]
    tour.append(city)
    all_cities.remove(city)
    while len(all_cities) != 0:
        min = 123324221
        for i in all_cities:
            distance = getDistance(nodeDict[city], nodeDict[i])
            if distance < min:
                min = distance
                nearest_city = i
        tour.append(nearest_city)
        all_cities.remove(nearest_city)
        city = nearest_city
    return tour

def starter():
    global cities
    takeInput()
    #print(cities)
    tour = getRandomTour()
    #min_tour = NearestNeighbourTour()
    #min_tour_length = getTourLength(min_tour)
    #print(tour)
    min_tour_length,min_tour = hillClimbFull(tour)
    drawPath(nodeDict, min_tour, min_tour_length)
    print(min_tour_length)
    print(min_tour)
starter()

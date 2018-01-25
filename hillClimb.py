import math
from random import shuffle

cities = 0

nodeDict = {}
class Node():
    def __init__(self,index, xc, yc):
        self.i = index
        self.x = xc
        self.y = yc


def takeInput():
    global cities
    f = open("data/a280",'r').read().splitlines()
    #tprint(f)

    cities = len(f)
    print(cities)
    for x in f:
        m = x.split()
        #print(m)
        m = [int(y) for y in m]
        #print (m[0])
        #print(m[1])
        #print(m[2])
        nodeDict[m[0]] = Node(m[0], m[1], m[2])
    print(len(nodeDict))
    return

step = 0
def hillClimbOneStep(tour):
    global step
    print(step)
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

    return min_tour_length

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

def starter():
    global cities
    takeInput()
    print(cities)
    tour = getRandomTour()
    
    print(tour)
    min_tour_length = hillClimbFull(tour)
    print(min_tour_length)
starter()

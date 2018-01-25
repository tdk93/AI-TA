import math

cities = 0
class Node():
    def __init__(self,index, xc, yc):
        self.i = index
        self.x = xc
        self.y = yc


def takeInput():
    f = open("data/a280",'r').read().splitlines()
    #print(f)
    NodeDict = {}

    for x in f:
        m = x.split()
        #print(m)
        m = [int(y) for y in m]
        #print (m[0])
        #print(m[1])
        #print(m[2])
        NodeDict[m[0]] = Node(m[0], m[1], m[2])
    return

takeInput()

def hillClimbOneStep(tour):
    possible_neighbours = get2OptNeighbours(tour)
    min_tour_length = getTourLength(tour)
    localMinima = True 
    for x in possible_neighbours:
        if getTourLength(x) < min_tour_length:
            localMinima = False 
            min_tour = x
            min_tour_length = getTourLength(x)

    return min_tour, min_tour_length, localMinima

def hillClimbFull(initial_tour):
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

    return

def get2OptNeighbours(order):
    final_neighbours = []
    for x in range(order.length()):
        for y in range(order.length()):
            if x != y:
                new_order = order[:x] + order[x:y][::-1] + order[y:]
                final_neighbours.append(new_order)
    return final_neighbours

def get3OptNeigbours(s):
    return

def getTourLength(tour):
    length = 0
    if tour.length == 2:
        return getDistance(tour[0],tour[1])

    for x in range(tour.length()-1):
        length += getDistance(tour[x],tour[x+1]) 
    
    length += getDistance(tour[0],tour[-1])

    return length

def getDistance(n1, n2):
    return math.sqrt((n1.x-n2.x)*(n1.x-n2.x) + (n1.y-n2.y)*(n1.y-n2.y))

def getRandomTour(s):
    return



import sys
import math
from random import shuffle
from draw import drawPath
import graph_plot
from collections import defaultdict
import argparse
import random
import itertools
from dd import *


cities = 0
nodeDict = {}

class Node():
    def __init__(self,index, xc, yc):
        self.i = index
        self.x = xc
        self.y = yc


def generateFile(cities, seed):
    MIN = 0
    MAX = 5000   
    random.seed(seed)
    i = 1
    filename = "tsp"+str(cities)
    with open(filename, "w") as f:
        for _ in itertools.repeat(None, cities):
            f.write("{p} {p0} {p1}\n".format(p=i, p0=random.randint(MIN, MAX), p1=random.randint(MIN, MAX)))
            i = i + 1
    return filename


def takeInput(file):
    global cities
    f = open(file,'r').read().splitlines()
    cities = len(f)
    for a in f:
        m = a.split()
        i = int(m[0])
        x = float(m[1])
        y = float(m[2])
        nodeDict[i] = Node(i, x, y)
    return


def generate2optNeighbours(tour):
    global cities
    all_possible_neighbours = []
    order = tour
    for x in range(len(order)):
        for y in range(len(order)):
            if x < y:
                #print(x)
                #print(y)
                new_order = order[:x] + order[x:y][::-1] + order[y:]
                #print(new_order)
                all_possible_neighbours.append(new_order)

    "*** YOUR CODE HERE ***"
    return all_possible_neighbours

def print2optNeighbours(tourList):
    pass



def generateRandomTour(r2seed):
    global cities
    print(cities)
    random.seed(r2seed)
    tour = [x for x in range(1,cities+1)]
    #print(tour)
    shuffle(tour)
    #print(tour)
    return tour

#-------------------------------------------------------------------------------------#
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

step = 0
def hillClimbOneStep(tour):
    global step
    #print(step)
    step += 1
    global cities
    possible_neighbours = generate2optNeighbours(tour)
    print(possible_neighbours)
    #possible_neighbours = get3OptNeighbours(tour)
    min_tour_length = getTourLength(tour)
    min_tour = 0
    localMinima = True 
    for x in possible_neighbours:
        if getTourLength(x) < min_tour_length:
            localMinima = False 
            min_tour = x
            min_tour_length = getTourLength(x)

    print(localMinima)
    return min_tour, min_tour_length, localMinima

def hillClimbFull(initial_tour):

    global cities
    tour_list = []
    change = True
    min_tour_length = 00000000
    min_tour = 0
    tour = initial_tour
    while True:
        tour, tour_length,localMinima = hillClimbOneStep(tour)
        if localMinima == True:
            #print("minimum tour found")
            break
        else:

            tour_list.append(tour_length)
            min_tour_length = tour_length
            min_tour = tour

    print(tour_list)
    return tour_list, min_tour

def nearestNeighbourTour(initial_city):
    tour = []
    all_cities = [x for x in range(1, cities + 1)]
    city = int(intial_city)#all_cities[0]
    tour.append(inital_city)
    all_cities.remove(city)
    while len(all_cities) != 0:
        mini = 123324221
        for i in all_cities:
            distance = getDistance(nodeDict[city], nodeDict[i])
            if distance < mini:
                mini = distance
                nearest_city = i
        tour.append(nearest_city)
        all_cities.remove(nearest_city)
        city = nearest_city
    return tour

def hillClimbWithNearestNeighbour(initial_city):
    tour = nearestNeighbourTour(initial_city)
    tour_length_list, tour_length = hillClimbFull(tour)
    generateGraph(tour_length_list)





#---------------------------------------------------------------------------------------------------------------

def hillClimbWithRandomTour(tour):
    """ Use the given tour as initial tour, Use your generate2optNeighbours() to generate
        all possible 2opt neighbours and apply hill climbing algorithm. Store the tour lengths
        that you are getting after every hill climb step in a list and pass it to the generateGraph(list)
        function. You will find 'task2.png' in current directory which shows hill climb algorithm performace
        that is hill climb iterations against tour length"""

    
    tourLengthList = []
    tourLengthList, minTour = hillClimbFull(tour)
    #print(minTour)
    #print(tourLengthList)


    "*** YOUR CODE HERE***"
    '''
    generateGraph(tourLengthlist)
    '''


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', action='store', dest='file', help="Provide a file name (if file given then no need to provide city and random seed option that is -n and -r)")
    parser.add_argument('-n', action='store', type=int, dest='cities', help="Provide number of cities in a tour")
    parser.add_argument('-r1', action='store', type=int, dest='r1seed', default=1, help="random seed")
    parser.add_argument('-r2', action='store', type=int, dest='r2seed', default=1, help="random seed")
    parser.add_argument('--task', '-t', action='store', type=int, dest="task", help="task to execute")
    args = parser.parse_args()

    if args.file:
        takeInput(args.file)
    elif args.cities:
        file = generate_file(args.cities, args.r1seed)
        takeInput(file)
    else:
        print("Please provide either a file or combination of number of cities and random seed")
        sys.exit()

    if not args.task:
        print("Please provide task number to execute")
        sys.exit()

    if args.task == 1:
        tour = generateRandomTour(args.r2seed)
        list1 = generate2optNeighbours(tour)

    if args.task == 2:
        tour = generateRandomTour(args.r2seed)
        hillClimbWithRandomTour(tour)


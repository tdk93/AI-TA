import sys
import math
from random import shuffle
from draw import drawPath
import graph_plot
from collections import defaultdict
import argparse
import random
import itertools


cities = 0
nodeDict = {}


def generate_file(cities, seed):
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
    all_possible_neighbours = []
    "*** YOUR CODE HERE ***"
    return all_possible_neighbours


def generateRandomTour(r2seed):
    random.seed(r2seed)
    tour = [x for x in range(1,cities+1)]
    shuffle(tour)
    return tour


def hillClimbWithRandomTour(tour):
    """ Use the given tour as initial tour, Use your generate2optNeighbours() to generate
        all possible 2opt neighbours and apply hill climbing algorithm. Store the tour lengths
        that you are getting after every hill climb step in a list and pass it to the generateGraph(list)
        function. You will find 'task2.png' in current directory which shows hill climb algorithm performace
        that is hill climb iterations against tour length"""

    tourLengthList = [1, 2, 3]
    "*** YOUR CODE HERE***"
    graph_plot.generateGraph(tourLengthlist)


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
        tour = generateRandomTour()
        print(tour)
        tourlist = generate2optNeighbours(tour)
        print(tourlist)

    if args.task == 2:
        tour = generateRandomTour()
        min_tour = hillClimbWithRandomTour(tour)

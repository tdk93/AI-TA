import sys
import math
from random import shuffle
from draw import drawPath
import graph_plot
from collections import defaultdict

cities = 0
nodeDict = {}
unionFind= [] 

class Node():
    def __init__(self,index, xc, yc):
        self.i = index
        self.x = xc
        self.y = yc

def euclidpapa():
    global unionFind
    for x in range(cities+1):
        unionFind.append(x)
    print(unionFind)
    print(unionFind[5])
    
    edges = defaultdict(dict) 
    edgeList = []
    for x in nodeDict:
        for y in nodeDict:
            #print("X is ")
            #print(x)
            if x != y:
                edges[x][y] = getDistance(nodeDict[x],nodeDict[y]) 
                edgeList.append([x,y,edges[x][y]])

    #print(edgeList[0:10])
    kruskal_set = []
    edgeList.sort(key=lambda x:int(x[2]))
    for x in edgeList:
        if(find(x[0],x[1]) == False):
            kruskal_set.append((x[0],x[1]))
            union(x[0],x[1])

    print(kruskal_set)
    fin_ord = construct_graph(kruskal_set)
    #fin_ord.append(1)
    return fin_ord
    print(fin_ord)

def construct_graph(kruskal_set):
    adj_list = defaultdict(list) 
    for x in kruskal_set:
        a,b = x
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    return dfs(adj_list)

def dfs(adj_list):
    final_order = []
    visited = {}
    for x in range(1,cities+1):
        visited[x] = False 
    dfs_util(1, adj_list, visited, final_order)
    return final_order


def dfs_util(node_val, adj_list, visited, final_order):
    visited[node_val] = True
    final_order.append(node_val)
    for x in adj_list[node_val]:
        if (visited[x] == False):
            dfs_util(x, adj_list, visited, final_order)




def union(x,y):
    k1 = unionFind[x]
    k2 = unionFind[y]
    for x in range(cities+1):
        if unionFind[x] == k1:
            unionFind[x] = k2


def find(x,y):
    return unionFind[x] == unionFind[y]

def takeInput():
    global cities
    #f = open(sys.argv[1],'r').read().splitlines()

    f = open("data/a280",'r').read().splitlines()
    #tprint(f)

    cities = len(f)
    #print(cities)
    for a in f:
        m = a.split()
        #print(m)
        #print(m)
        i = int(m[0])
        x = float(m[1])
        y = float(m[2])
        #m = [float(y) for y in m]
        #m = [int(y) for y in m]
        #print (m[0])
        #print(m[1])
        #print(m[2])
        nodeDict[i] = Node(i, x, y)
    #print(len(nodeDict))
    return

step = 0
def hillClimbOneStep(tour):
    global step
    #print(step)
    step += 1
    global cities
    possible_neighbours = get2OptNeighbours(tour)
    #possible_neighbours = get3OptNeighbours(tour)
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
    tour_list = []
    change = True
    min_tour_length = 00000000
    min_tour = 0
    tour = initial_tour
    while True:
        tour, tour_length,localMinima = hillClimbOneStep(tour)
        tour_list.append(tour_length)
        if localMinima == True:
            #print("minimum tour found")
            break
        else:
            min_tour_length = tour_length
            min_tour = tour

    return min_tour_length, min_tour, tour_list

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

def HillClimbWithInitialRandomTour(iterations):
    all_lists = []
    avg_list = []
    for i in range(iterations):
        tour = getRandomTour()
        min_tour_length,min_tour, tour_list = hillClimbFull(tour)
        print(tour_list)
        all_lists.append(tour_list)
    
    min = len(all_lists[0])
    for i in range(1, iterations):
        if (len(all_lists[i]) < min):
            min = len(all_lists[i])
    for i in range(3):
        all_lists[i] = all_lists[i][0:min]

    for i in range(min):
        avg = 0
        for j in range(iterations):
            avg = avg + all_lists[j][i]
        avg_list.append(avg/iterations)
    print(avg_list)
    graph_plot.plot(avg_list)


def HillClimbWithInitialNearestNeighbourTour():
    tour = NearestNeighbourTour()
    min_tour_length,min_tour, tour_list = hillClimbFull(tour)
    graph_plot.plot(tour_list)

def starter():
    global cities
    takeInput()


    HillClimbWithInitialRandomTour(3)
    HillClimbWithInitialNearestNeighbourTour()
    graph_plot.save("a.png")
    #drawPath(nodeDict, min_tour, min_tour_length)


    #print(cities)
    #tour = getRandomTour()
    #print(tour)
    tour = euclidpapa()
    #min_tour = NearestNeighbourTour()
    #min_tour_length = getTourLength(min_tour)
    #print(tour)
    min_tour_length,min_tour = hillClimbFull(tour)
    #drawPath(nodeDict, min_tour, min_tour_length)
    print(min_tour_length)
    print(min_tour)

starter()
#euclidpapa()

import matplotlib.pyplot as plt
import numpy as np

x = 0
y = 0
z = 0

def plot_random(b):
	global x
	a = list(range(len(b)))
	plt.xlabel('hill climb iterations')
	plt.ylabel('tour length')
	handle1, = plt.plot(a, b, label='random')
	x = handle1

def plot_euclidean(b):
	global y
	a = list(range(len(b)))
	plt.xlabel('hill climb iterations')
	plt.ylabel('tour length')
	handle2, = plt.plot(a, b, label='euclidean')
	y = handle2

def plot_nearest_neighbour(b):
	global z
	a = list(range(len(b)))
	plt.xlabel('hill climb iterations')
	plt.ylabel('tour length')
	handle3, = plt.plot(a, b, label='nearest_neighbour')
	z = handle3

def save(filename):
	#plt.legend(handles=[x, y, z])

	plt.legend(handles=[y, z])
	plt.savefig(filename)

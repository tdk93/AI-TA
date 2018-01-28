import matplotlib.pyplot as plt
import numpy as np

def plot(b):
	#print(b)
	a = list(range(len(b)))
	plt.xlabel('hill climb iterations')
	plt.ylabel('tour length')
	plt.plot(a, b)

def save(filename):
	plt.savefig(filename)

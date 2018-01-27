#!/usr/bin/env python3
"""Generate randomized input files, in the expected format."""

import itertools
from random import randint

MIN = 0
MAX = 500

def generate_input(n, filename):
    i = 1
    with open(filename, "w") as f:
        #f.write("{n}\n".format(n=n))
        for _ in itertools.repeat(None, n):
            f.write("{p} {p0} {p1}\n".format(p=i, p0=randint(MIN, MAX), p1=randint(MIN, MAX)))
            i = i + 1

if __name__ == "__main__":
    # Write the input files for the optimal solution first.
    n = 6
    generate_input(n, "tsp6.txt")
    n = 9
    generate_input(n, "tsp9.txt")
    n = 10
    generate_input(n, "tsp10.txt")
    # Then write the input files for nearest neighbor.
    n = 50
    generate_input(n, "tsp50.txt")
    n = 100
    generate_input(n, "tsp100.txt")
    n = 200
    generate_input(n, "tsp200.txt")

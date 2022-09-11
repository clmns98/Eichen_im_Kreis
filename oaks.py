import random as rn
import numpy as np

# number of oaks
n = 4

# number of spots
number_spots = n*(n-1)+1

print(f"n = {n}\nnumber of spots {number_spots}\n")

# define circle
circle = np.zeros(number_spots)

def insert_oaks(circle):
    # oaks represented as numbers
    for i in range(1, n+1):
        insert_spot(circle, i)

def insert_spot(circle, i):
    # generate a random spot
    spot = rn.randint(1, number_spots-1)
    # check if spot is empty
    if circle[spot] == 0:
        # insert an oak into spot
        circle[spot] = i
    else:
        # call function again if taken
        insert_spot(circle, i)

def check_circle(circle):

    # counts the distances between oaks
    counter = 0

    # distances between oaks
    dist_list = []

    # set true if first oak found
    first_found = False

    for i in circle:
        if i != 0:
            if first_found:
                counter += 1
                dist_list.append(i)
            else:
                first_found = True
                counter = 0
                
        else:
            counter += 1
    
    return dist_list


def main():
    for i in range(9):
        circle = np.zeros(number_spots)
        insert_oaks(circle)
        print(circle)
        print(check_circle(circle))
        print()

main()
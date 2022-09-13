import random as rn
import numpy as np
import time

# https://followthescore.org/schueler-labor/eichen-im-kreis/

def gaussian_sum_formula(n):
    return int((n*(n-1)/2))

def generate_circle(spots, n):
    
    # define circle
    circle = np.zeros(spots, dtype=int)

    # oaks represented as numbers
    for i in range(1, n+1):
        insert_spot(circle, i, spots)

    return circle

def insert_spot(circle, i, spots):

    # generate a random spot
    spot = rn.randint(0, spots-1)

    # check if spot is empty
    if circle[spot] == 0:

        # insert an oak into spot
        circle[spot] = i

    else:
        # call function again if taken
        insert_spot(circle, i, spots)

def get_outer_dist(spaces,n):
    
    sum = 0
    
    for i in range(n-1):
        sum += spaces[i]

    return sum

def get_spaces(circle, n):

    # count steps between oaks
    steps = 0

    counter = 0

    # list of spaces between oaks
    spaces = np.zeros(n, dtype=int)

    # set true if first oak was found
    first_found = False

    for i in circle:
        # breakpoint()
        if i != 0:
            if first_found:
                steps += 1
                spaces[counter] = steps
                counter += 1
                steps = 0
            else:
                first_found = True
                steps = 0
                
        else:
            steps += 1

    spaces[-1] = get_outer_dist(spaces, n)

    return spaces

def get_distances(spaces, n):
    # get the distance from every oak to every other oak

    gaussian_sum = gaussian_sum_formula(n)

    distances = np.zeros(gaussian_sum*2, dtype=int)

    counter = 0
    
    for i in range(len(spaces)):
        for j in range(i + 1, len(spaces) + 1):
            distances[counter] = sum(spaces[i:j])
            counter += 1
    
    # calculate distances the other way around
    for i in range(gaussian_sum, gaussian_sum*2):
        distances[i] = distances[i - gaussian_sum]

    return distances

def check_circle(circle, n):

    # get the spaces between the oaks
    distances = get_distances(get_spaces(circle, n), n)
    #print(distances)

    # this part needs rework!!!
    if np.all(np.unique(distances) == distances):
        return True
    else:
        return False

def main():
    start_time = time.time()

    # number of oaks
    n = 4

    # number of spots
    spots = n*(n-1)+1

    print(f"\nn = {n}\nnumber of spots {spots}")

    not_found = True

    #for i in range(400):
    while not_found:

        # put oaks into circle
        circle = generate_circle(spots, n)
        #print(circle)

        # checks if all trees have different distances
        if check_circle(circle, n):

            # print the correct circle
            print(circle)

            # end search for circle
            not_found = False
    
    print(f"\ntime needed: {time.time()-start_time:.4f}s\n")

main()
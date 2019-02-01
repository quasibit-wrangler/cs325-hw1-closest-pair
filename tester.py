import helperLibrary as h
import parta as bruteForce
import partb as naive
import partc as best
import sys

import time
import profiler as p




def main():

    worker = None

    if(sys.argv[1] == "brute"):
        worker = bruteForce.bruteForce
    elif(sys.argv[1] == "naive"):
        worker = naive.naiveApproach
    elif(sys.argv[1] == "advanced"):
        worker = best.advancedApproach
    else:
        raise Exception("Invalid algorythem selection, please select: brute | naive | advanced ")

    if(sys.argv[2] == "1" or sys.argv[2] == "2" or sys.argv[2] == "3" or sys.argv[2] == "4" or sys.argv[2] == "5"):
        for i in range(10):
            points = h.grabArray("./files/size{}/file{}.txt".format(sys.argv[2],i))
            # points = h.grabArray()
            start_time = time.time()

            results = worker(points)

            e = int(time.time() - start_time)

            results = h.clean_duplicates_map(results)
            h.printResults(results,h.dist_between_points(results[0][0],results[0][1]))
            print('{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))
            print('\n')

        p.print_prof_data()
    else:
        # the 2nd argument passed into the function
        # will be the local filepath the TA specifies
        points = h.grabArray(sys.argv[2])
        results = worker(points)

        results = h.clean_duplicates_map(results)
        h.printResults(results,h.dist_between_points(results[0][0],results[0][1]))






main()

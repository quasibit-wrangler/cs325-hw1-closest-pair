import helperLibrary as h
import profiler as p

@p.profile
def bruteForce(messyStuff):
    current_best = None
    for index,item in enumerate(messyStuff):
        for OtherItem in messyStuff[index+1:]:
            # looks at the items and creates a new array the new correct set.
            current_best = h.min_distance(current_best,[[item,OtherItem]])
    return current_best



def main():
    # points = h.grabArray()

    for i in range(10):
        points = h.grabArray("./files/size1/file{}.txt".format(i))
        results = bruteForce(points)
        h.printResults(results,h.dist_between_points(results[0][0],results[0][1]))
        print('\n')


    p.print_prof_data()






main()

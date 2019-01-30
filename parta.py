import helperLibrary as h
import profiler as p
import time

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
        points = h.grabArray("./files/size4/file{}.txt".format(i))
        # points = h.grabArray()

        start_time = time.time()

        results = bruteForce(points)

        e = int(time.time() - start_time)
        h.printResults(results,h.dist_between_points(results[0][0],results[0][1]))
        print('{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))
        print('\n')

    p.print_prof_data()






main()

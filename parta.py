import helperLibrary as h



def bruteForce(messyStuff):
    current_best = None
    for index,item in enumerate(messyStuff):
        for OtherItem in messyStuff[index+1:]:
            current_best = h.min_distance(current_best,[[item,OtherItem]])
    return current_best



def main():
    points = h.grabArray()
    results = bruteForce(points)
    h.printResults(results,h.dist_between_points(results[0][0],results[0][1]))







main()

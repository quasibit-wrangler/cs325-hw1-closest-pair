import helperLibrary as helperfoos

def naiveApproach(messyStuff):
    #sort by x for the first time
    messyStuff.sort(key=lambda point: point[0])
    sortByX = messyStuff
    results = split(sortByX)

    return results

def scanEntireArray(array):
    return None

# p1 and p2 are pairs of points or many pairs of points
#return the min of the two
def min_point(p1,p2):
    if(p1==None):
        return p2
    elif(p2==None):
        return p1
    elif(helperfoos.dist_between_points(p1[0][0],p1[0][1])<
        helperfoos.dist_between_points(p2[0][0],p2[0][1])):
        return p1
    elif(helperfoos.dist_between_points(p1[0][0],p1[0][1])==
        helperfoos.dist_between_points(p2[0][0],p2[0][1])):
        for item in p2:
            p1.append(item)
        return p1
    else:
        return p2

def min_distance(p1, p2):
    if(p1==None):
        return p2
    elif(p2==None):
        return p1
    minDistance1 = helperfoos.dist_between_points(p1[0], p1[1])
    minDistance2 = helperfoos.dist_between_points(p2[0], p2[1])
    if(minDistance1<minDistance2):
        return p1
    elif(minDistance1==minDistance2):
        for item in p2:
            p1.append(item)
        return p1
    else:
        return p2


def split(Array):
    print(Array)
    if(len(Array)==1):
        return (None)
    elif(len(Array)==2):
        print("len 2 base case", Array)
        return Array
    else:
        midPoint = len(Array)/2
        closest1 = min_distance(split(Array[:midPoint]),split(Array[midPoint:]))
        Array.sort(key=lambda point: point[1]) #sort by the second element
        print ("closest1: ", closest1)
        closest0 = scanEntireArray(Array)

        return closest1




def main():
    points = helperfoos.grabArray()
    results=naiveApproach(points)
    print("Final Result", results)
    #helperfoos.printResults(results,helperfoos.dist_between_points(results[0][0],results[0][1]))







main()

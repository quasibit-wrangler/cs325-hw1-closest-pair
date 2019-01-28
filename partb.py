import helperLibrary as helperfoos

def naiveApproach(messyStuff):
    #sort by x for the first time
    messyStuff.sort(key=lambda x: x[0])
    sortByX = messyStuff
    print(sortByX)
    results = split(sortByX)

    return results

def scanEntireArray(array):

    return

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




def split(Array):
    if(len(Array)==1):
        return (None)
    elif(len(Array)==2):
        return Array
    else:
        closest1 = min_point(split(Array[:len(Array)/2]),split(Array[len(Array/2)+1:]))
        Array.sort(key=lambda x: x[1]) #sort by the second element
        closest0 = scanEntireArray(array)

        return closest0 if(closest0<closest1) else closest1




def main():
    points = helperfoos.grabArray()
    results=naiveApproach(points)
    helperfoos.printResults(results,helperfoos.dist_between_points(results[0][0],results[0][1]))







main()

import helperLibrary as helperfoos
import copy as c
import profiler as p

@p.profile
def advancedApproach(messyStuff):
    #sort by x for the first time
    messyStuff.sort(key=lambda point: point[0])
    sortByX = messyStuff
    sortedYArray = c.deepcopy(sortByX)
    sortedYArray.sort(key=lambda point: point[1])

    results = split(sortByX, sortedYArray)

    return results

def findDelta(currentArray,currentBestDistance):
    # if(len(currentArray)%2==0):
    medianX = currentArray[len(currentArray)/2][0]
    subArray={}
    for i in range(len(currentArray)):
        if(abs(currentArray[i][0]-medianX)<=currentBestDistance):
            subArray["{x},{y}".format(x=currentArray[i][0], y=currentArray[i][1])] = True
    return subArray


#"{x},{y}".format(x=array[0],y=array[1])
def scanEntireArray(array,currentBest,sortedYArray):
    currentLength=helperfoos.dist_between_points(currentBest[0][0],currentBest[0][1])
    subArray = findDelta(array,currentLength)
    sortedSubArray = []
    for point in sortedYArray:
        key = "{x},{y}".format(x=point[0], y=point[1])
        if key in subArray:
            sortedSubArray.append(point)
    #brute force the check but discard y values that are crappy.
    for index in range(0,len(sortedSubArray)):
        for index2 in range(index+1,len(sortedSubArray)):
            length_y=sortedSubArray[index2][1]-sortedSubArray[index][1]
            if(length_y>currentLength):
                #there is no way this index1 has a closest pair
                break
            else:
                p2=[(sortedSubArray[index],sortedSubArray[index2])]
                currentBest = helperfoos.min_distance(currentBest,p2)
        pass
    return currentBest


def split(sortedXArray, sortedYArray):
    if(len(sortedXArray)==1):
        return (None)
    elif(len(sortedXArray)==2):
        return [(sortedXArray[0], sortedXArray[1])]
    else:
        midPoint = len(sortedXArray)/2
        closest1 = helperfoos.min_distance(split(sortedXArray[:midPoint], sortedYArray),split(sortedXArray[midPoint:], sortedYArray))
        closest0 = scanEntireArray(sortedXArray,closest1, sortedYArray)
        return closest0

def turntoArray(tuples):
    clean_array = []
    for item in tuples:
        clean_array.append([ [item[0][0],item[0][1] ], [ item[1][0],item[1][1] ] ])
    return clean_array

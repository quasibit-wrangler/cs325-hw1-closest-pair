import helperLibrary as helperfoos
import profiler as p
import time


@p.profile
def naiveApproach(messyStuff):
    #sort by x for the first time
    messyStuff.sort(key=lambda point: point[0])

    sortByX = messyStuff
    results = split(sortByX)

    return results


def split(sortedXArray):
    if(len(sortedXArray)==1):
        return (None)
    elif(len(sortedXArray)==2):
        return [[sortedXArray[0], sortedXArray[1]]]
    else:
        midPoint = len(sortedXArray)/2
        closest1 = helperfoos.min_distance(split(sortedXArray[:midPoint]),split(sortedXArray[midPoint:]))
        closest0 = scanEntireArray(sortedXArray,closest1)
        return closest0


def findDelta(sortedXArray,currentBestDistance,medianX):
    subArray=[]
    for i in range(len(sortedXArray)):
        if(abs(sortedXArray[i][0]-medianX)<=currentBestDistance):
            subArray.append(sortedXArray[i])
    return subArray

def scanEntireArray(sortedXArray,currentBest):
    currShortDistance = helperfoos.dist_between_points(currentBest[0][0],currentBest[0][1])
    medianX = sortedXArray[len(sortedXArray)/2][0]
    subArray = findDelta(sortedXArray,currShortDistance,medianX)
    sortedYArray = sorted(subArray,key=lambda point: point[1]) #sort by the second element

    #brute force the check but discard y values that are crappy.
    for index in range(0,len(sortedYArray)):
        for index2 in range(index+1,len(sortedYArray)):
            length_y=sortedYArray[index2][1]-sortedYArray[index][1]
            if(length_y>currShortDistance):
                #there is no way this index1 has a closest pair
                break
            else:
                #there is a posibility that these points are shorter distanceself
                # than our current set of pairs
                p2=[[sortedYArray[index],sortedYArray[index2]]]
                currentBest = helperfoos.min_distance(currentBest,p2)
        pass
    return currentBest

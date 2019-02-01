import helperLibrary as helperfoos
import copy as c
import profiler as p
import time

@p.profile
def advancedApproach(messyStuff):
    #sort by x for the first time
    messyStuff.sort(key=lambda point: point[0])

    sortByX = messyStuff
    sortedYArray = sorted(c.deepcopy(sortByX),key=lambda point: point[1])

    results = split(sortByX,sortedYArray)

    return results


def split(sortedXArray,sortedYArray):
    if(len(sortedXArray)==1):
        return (None)
    elif(len(sortedXArray)==2):
        return [[sortedXArray[0], sortedXArray[1]]]
    else:
        midPoint = len(sortedXArray)/2
        midxValue = sortedXArray[midPoint][0]
        # try and shrink the array each time.
        sortedYArray_l =  filterSortedY(sortedYArray,midxValue,0)
        sortedYArray_r = filterSortedY(sortedYArray,midxValue,1)

        closest1 = helperfoos.min_distance(split(sortedXArray[:midPoint],sortedYArray_l),split(sortedXArray[midPoint:],sortedYArray_r))
        closest0 = scanEntireArray(sortedXArray,closest1,sortedYArray)
        return closest0


def findDelta(sortedXArray,currentBestDistance,medianX):
    # if(len(currentArray)%2==0):
    subArray=[]
    for i in range(len(sortedXArray)):
        if(abs(sortedXArray[i][0]-medianX)<=currentBestDistance):
            subArray.append(sortedXArray[i])
    return subArray


# if sign == 1, all items must be above x value
# else the nit has to be below x value
def filterSortedY(sortedYArray,xValue,sign):
    filterd_sortedY = []
    for item in sortedYArray:
        if(sign == 1):
            if(item[0] >= xValue):
                filterd_sortedY.append(item)
        else:
            if(item[0] <= xValue):
                filterd_sortedY.append(item)

    return filterd_sortedY


def scanEntireArray(sortedXArray,currentBest,sortedYArray):
    currShortDistance = helperfoos.dist_between_points(currentBest[0][0],currentBest[0][1])
    medianX = sortedXArray[len(sortedXArray)/2][0]
    sorted_y_subArray = findDelta(sortedYArray,currShortDistance,medianX)
    # sortedYArray = sorted(subArray,key=lambda point: point[1]) #sort by the second element

    #brute force the check but discard y values that are crappy.
    for index in range(0,len(sorted_y_subArray)):
        for index2 in range(index+1,len(sorted_y_subArray)):
            length_y=sorted_y_subArray[index2][1]-sorted_y_subArray[index][1]
            if(length_y>currShortDistance):
                #there is no way this index1 has a closest pair
                break
            else:
                #there is a posibility that these points are shorter distanceself
                # than our current set of pairs
                p2=[[sorted_y_subArray[index],sorted_y_subArray[index2]]]
                currentBest = helperfoos.min_distance(currentBest,p2)
        pass
    return currentBest

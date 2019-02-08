import helperLibrary as helperfoos
import copy as c
import profiler as p
import time


@p.profile
def advancedApproach(messyStuff):
    #sort by x for the first time

    messyStuff.sort(key=lambda point: point[0])
    sortByX = messyStuff
    sortedYArray = c.deepcopy(sortByX)
    sortedYArray.sort(key=lambda point: point[1])


    results = split(sortByX, sortedYArray)

    return results

# if sign == 1, all items must be above x value
# else the nit has to be below x value
def filterSortedY(sortedYArray,xValue,newArray):
    for item in sortedYArray:
        if(item[0]<xValue):
            newArray[0].append(item)
        else:
            newArray[1].append(item)

def split(sortedXArray, sortedYArray):
    if(len(sortedXArray)==1):
        return (None)
    elif(len(sortedXArray)==2):
        return [(sortedXArray[0], sortedXArray[1])]
    else:
        midPoint = len(sortedXArray)/2
        midxValue = sortedXArray[midPoint][0]
        l_and_r=[[],[]]
        filterSortedY(sortedYArray,midxValue,l_and_r)
        closest1 = helperfoos.min_distance(split(sortedXArray[:midPoint],l_and_r[0]),split(sortedXArray[midPoint:],l_and_r[1]))
        # closest1 = helperfoos.min_distance(split(sortedXArray[:midPoint],sortedYArray),split(sortedXArray[midPoint:],sortedYArray))
        closest0 = scanEntireArray(sortedXArray,closest1,sortedYArray)
    return closest0

def findDelta(sortedYArray,currentBestDistance,bounds):
    # if(len(currentArray)%2==0):
    subArray=[]
    for i in range(len(sortedYArray)):
        if(abs(sortedYArray[i][0]-bounds[1])<=currentBestDistance):
            subArray.append(sortedYArray[i])
    return subArray


#"{x},{y}".format(x=array[0],y=array[1])
#bounds = [ sortx[0], medianX, sortx[-1]]
def scanEntireArray(sortedXArray,currentBest,sortedYArray):
    currShortDistance=helperfoos.dist_between_points(currentBest[0][0],currentBest[0][1])
    bounds=[ sortedXArray[0][0],sortedXArray[len(sortedXArray)/2][0],sortedXArray[-1][0]]
    sorted_byY_SubArray = findDelta(sortedYArray,currShortDistance,bounds)
    #brute force the check but discard y values that are crappy.
    for index in range(0,len(sorted_byY_SubArray)):
        for index2 in range(index+1,len(sorted_byY_SubArray)):
            length_y=sorted_byY_SubArray[index2][1]-sorted_byY_SubArray[index][1]
            if(length_y>currShortDistance):sortedXArray
                #there is no way this index1 has a closest pair
                break
            else:
                p2=[(sorted_byY_SubArray[index],sorted_byY_SubArray[index2])]
                currentBest = helperfoos.min_distance(currentBest,p2)
        pass
    return currentBest








def turntoArray(tuples):
    clean_array = []
    for item in tuples:
        clean_array.append([ [item[0][0],item[0][1] ], [ item[1][0],item[1][1] ] ])
    return clean_array

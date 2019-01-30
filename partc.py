import helperLibrary as helperfoos

def naiveApproach(messyStuff):
    #sort by x for the first time
    messyStuff.sort(key=lambda point: point[0])
    sortByX = messyStuff
    sortedYArray = messyStuff
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
    print(subArray)
    for point in sortedYArray:
        key = "{x},{y}".format(x=point[0], y=point[1])
        if key in subArray:
            sortedSubArray.append(point)
    #brute force the check but discard y values that are crappy.
    for index in range(0,len(subArray)):
        for index2 in range(index+1,len(sortedSubArray)):
            length_y=sortedSubArray[index2][1]-sortedSubArray[index][1]
            if(length_y>currentLength):
                #there is no way this index1 has a closest pair
                break
            else:
                p2=[(sortedSubArray[index],sortedSubArray[index2])]
                currentBest = min_distance(currentBest,p2)
        pass
    return currentBest

# p1 and p2 are pairs of points or many pairs of points
#return the min of the two
def min_distance(p1, p2):
    if(p1==None):
        return p2
    elif(p2==None):
        return p1
    print(p1,"comparing with",p2)
    minDistance1 = helperfoos.dist_between_points(p1[0][0], p1[0][1])
    minDistance2 = helperfoos.dist_between_points(p2[0][0], p2[0][1])
    if(minDistance1<minDistance2):
        print("choosing",p1)
        return p1
    elif(minDistance1==minDistance2):
        for item in p2:
            p1.append(item)
        print("equal", p1)
        return p1
    else:
        print("choosing", p2)
        return p2

    

def split(sortedXArray, sortedYArray):
    print(sortedXArray)
    if(len(sortedXArray)==1):
        return (None)
    elif(len(sortedXArray)==2):
        return [(sortedXArray[0], sortedXArray[1])]
    else:
        midPoint = len(sortedXArray)/2
        closest1 = min_distance(split(sortedXArray[:midPoint], sortedYArray),split(sortedXArray[midPoint:], sortedYArray))
        closest0 = scanEntireArray(sortedXArray,closest1, sortedYArray)
        return closest0




def main():
    points = helperfoos.grabArray()
    results=naiveApproach(points)
    helperfoos.clean_duplicates(results)
    print("Final Result", results)
    #helperfoos.printResults(results,helperfoos.dist_between_points(results[0][0],results[0][1]))







main()

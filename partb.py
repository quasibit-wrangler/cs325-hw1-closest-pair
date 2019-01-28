import helperLibrary as helperfoos

def naiveApproach(messyStuff):
    #sort by x for the first time
    messyStuff.sort(key=lambda point: point[0])
    sortByX = messyStuff
    results = split(sortByX)

    return results

def findDelta(currentArray,currentBestDistance):
    # if(len(currentArray)%2==0):
    medianX = currentArray[len(currentArray)/2][0]
    subArray=[]
    for i in range(len(currentArray)):
        if(abs(currentArray[i][0]-medianX)<=currentBestDistance):
            subArray.append(currentArray[i])
    return subArray

def scanEntireArray(array,currentBest):
    currentLength=helperfoos.dist_between_points(currentBest[0][0],currentBest[0][1])
    subArray = findDelta(array,currentLength)
    subArray.sort(key=lambda point: point[1]) #sort by the second element

    #brute force the check but discard y values that are crappy.
    for index in range(0,len(subArray)):
        for index2 in range(index+1,len(subArray)):
            length_y=subArray[index2][1]-subArray[index][1]
            if(length_y>currentLength):
                #there is no way this index1 has a closest pair
                break
            else:
                p2=[(subArray[index],subArray[index2])]
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

def clean_duplicates(pairArray):
    for pair1 in pairArray:
        for j, pair2 in enumerate(pairArray):
            if pair1[0][0] == pair2[0][0] and pair1[0][1] == pair2[0][1] and pair1[1][0] == pair2[1][0] and pair1[1][1] == pair2[1][1]:
                   del pairArray[j]
                   break

def split(Array):
    print(Array)
    if(len(Array)==1):
        return (None)
    elif(len(Array)==2):
        return [(Array[0], Array[1])]
    else:
        midPoint = len(Array)/2
        closest1 = min_distance(split(Array[:midPoint]),split(Array[midPoint:]))
        closest0 = scanEntireArray(Array,closest1)
        return closest0




def main():
    points = helperfoos.grabArray()
    results=naiveApproach(points)
    clean_duplicates(results)
    print("Final Result", results)
    #helperfoos.printResults(results,helperfoos.dist_between_points(results[0][0],results[0][1]))







main()

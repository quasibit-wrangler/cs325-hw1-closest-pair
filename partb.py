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
    currentLength = helperfoos.dist_between_points(currentBest[0][0],currentBest[0][1])
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
                p2=[[subArray[index],subArray[index2]]]
                currentBest = helperfoos.min_distance(currentBest,p2)
        pass
    return currentBest


def split(Array):
    if(len(Array)==1):
        return (None)
    elif(len(Array)==2):
        return [[Array[0], Array[1]]]
    else:
        midPoint = len(Array)/2
        closest1 = helperfoos.min_distance(split(Array[:midPoint]),split(Array[midPoint:]))
        closest0 = scanEntireArray(Array,closest1)
        return closest0




def main():
    points = helperfoos.grabArray()
    results=naiveApproach(points)
    helperfoos.clean_duplicates(results)
    helperfoos.printResults(results,helperfoos.dist_between_points(results[0][0],results[0][1]))







main()

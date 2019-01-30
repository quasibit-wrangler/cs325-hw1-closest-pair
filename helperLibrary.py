import sys
import math
import random


#returns the new array of points from two different dist_between_points
#inputs: 2 3 dimensional arrays, an array of pairs of pairs
# [ [[ x1,y1 ] [x2,y2]] ]
def min_distance(pair_set1, pair_set2):
    if(pair_set1==None):
        return pair_set2
    elif(pair_set2==None):
        return pair_set1
    minDistance1 = dist_between_points(pair_set1[0][0], pair_set1[0][1])
    minDistance2 = dist_between_points(pair_set2[0][0], pair_set2[0][1])
    if(minDistance1<minDistance2):
        return pair_set1
    elif(minDistance1==minDistance2):
        for item in pair_set2:
            pair_set1.append(item)
        return pair_set1
    else:
        return pair_set2


def grabArray():
    with open(sys.argv[1]) as f:
        content = f.readlines()

    numList = []
    # tuples = content.split('\n')
    for i in range(len(content)):
        content[i].rstrip("\n")
        numList.append(content[i].split())
        numList[len(numList)-1][0]=int(numList[len(numList)-1][0])
        numList[len(numList)-1][1]=int(numList[len(numList)-1][1])
    return numList
def grabArray(filename):
    with open(filename) as f:
        content = f.readlines()

    numList = []
    # tuples = content.split('\n')
    for i in range(len(content)):
        content[i].rstrip("\n")
        numList.append(content[i].split())
        numList[len(numList)-1][0]=int(numList[len(numList)-1][0])
        numList[len(numList)-1][1]=int(numList[len(numList)-1][1])
    return numList


def dist_between_points(p1,p2):
    x=p2[0]-p1[0]
    y=p2[1]-p1[1]
    return math.sqrt(x**2 + y**2)

def clean_duplicates(array):
    ## haha recusive function with no base case
    # i sure hope eventually we run out of duplicates!
    for i,pair1 in enumerate(array):
        for j in range(i+1,len(array)):
            if(  pair1[0][0] == array[j][0][0] and
                 pair1[0][1] == array[j][0][1] and
                 pair1[1][0] == array[j][1][0] and
                 pair1[1][1] == array[j][1][1] ):
                 del array[i]
                 array = clean_duplicates(array)
                 return array
    return array


def printResults(array,distance):
    print(distance)
    array.sort(key=lambda x: x[0][1])
    array.sort(key=lambda x: x[0][0])
    for item in array:
        item.sort(key=lambda x: x[1])
        print("{x1} {y1} {x2} {y2}".format(x1= item[0][0], y1=item[0][1], x2=item[1][0], y2=item[1][1]))
    return


# creates data file with specified parameters

#x and y values ranging from [-number_size_range, number_size_range]
# number of coordinate pairs == number_pairs
def createTestFile(file_name,number_size_range,number_pairs):
    with open(file_name, 'w') as file:
        for i in range ( number_pairs ):
            int1 = random.randint(-1*number_size_range,1+number_size_range)
            int2 = random.randint(-1*number_size_range,1+number_size_range)
            file.write("{x} {y}\n".format(x=int1, y=int2))

    return

import sys
import math

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


def dist_between_points(p1,p2):
    x=p2[0]-p1[0]
    y=p2[1]-p1[1]
    return math.sqrt(x**2 + y**2)


def printResults(array,distance):
    print(distance)
    array.sort(key=lambda x: x[0][1])
    array.sort(key=lambda x: x[0][0])

    for item in array:
        item.sort(key=lambda x: x[1])
        print("{x1} {y2} {x2} {y2}".format(x1= item[0][0], y1=item[0][1], x2=item[1][0], y2=item[1][1]))
    return

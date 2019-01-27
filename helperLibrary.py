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

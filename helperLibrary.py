import sys
import math
import random
import profiler as p


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


def grabArray(filename=None):
    if(filename == None):
        with open(sys.argv[1]) as f:
            content = f.readlines()
    else:
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



def clean_duplicates_map(array):
    singular = {}
    fresh = []
    for i,pair in enumerate(array):
        singular["{x},{y} {x2},{y2}".format(x=pair[0][0],y=pair[0][1],x2=pair[1][0],y2=pair[1][1])]=True

    for key in singular:
        twoitems = key.split()
        oneitem = [ twoitems[0].split(','), twoitems[1].split(',') ]
        p1x =int(oneitem[0][0])
        p1y = int(oneitem[0][1])
        p2x =int(oneitem[1][0])
        p2y = int(oneitem[1][1])
        oneitem= [ [p1x,p1y] , [p2x,p2y]  ]
        fresh.append(oneitem)

    return fresh


def printResults(array,distance):
    print(distance)
    array.sort(key=lambda x: x[0][1])
    array.sort(key=lambda x: x[0][0])
    for item in array:
        item.sort(key=lambda x: x[1])
        print("{x1} {y1} {x2} {y2}".format(x1= item[0][0], y1=item[0][1], x2=item[1][0], y2=item[1][1]))
    return


# creates data file with specified parameters
def uniquifyList(seq, idfun=None):
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

#x and y values ranging from [-number_size_range, number_size_range]
# number of coordinate pairs == number_pairs
def createTestFile(file_name,number_size_range,number_pairs):
    n = number_size_range
    N = number_pairs
    int1 = (random.randint(-1*n,1+n))
    int2 = (random.randint(-1*n,1+n))
    points = {(int1, int2) for i in xrange(N)}
    while len(points) < N:
        int1 = (random.randint(-1*n,1+n))
        int2 = (random.randint(-1*n,1+n))
        points |= {(int1, int2)}
    final_list = list(list(x) for x in points)

    with open(file_name, 'w') as file:
        for item in final_list:
            file.write("{x} {y}\n".format(x=item[0], y=item[1]))

    return

in the advanced approach, I had a typo rather than a logic error made that im surprized
didnt show up as a runtime error.


in this code block:
```python
#"{x},{y}".format(x=array[0],y=array[1])
#bounds = [ sortx[0], medianX, sortx[-1]]
def scanEntireArray(sortedXArray,currentBest,sortedYArray):
    currShortDistance=helperfoos.dist_between_points(currentBest[0][0],currentBest[0][1])
    bounds=[ sortedXArray[0][0],[len(sortedXArray)/2][0],sortedXArray[-1][0]]
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
```

on line 5:
```python
     bounds=[ sortedXArray[0][0],[len(sortedXArray)/2][0],sortedXArray[-1][0]]
```
bounds is the data structure to filter our all the y values in the findDelta()
function that finds the strip. however bounds[1] is supposed to be the middle x value
in the ``` sortedXArray ``` list yet for some reason the array name wasnt there???

the line should instead be:


on line 5:
```python
     bounds=[ sortedXArray[0][0],sortedXArray[len(sortedXArray)/2][0],sortedXArray[-1][0]]
```


im not sure how this typo didnt throw an errow becasue i was dereferencing blank space?

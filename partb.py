import helperLibrary as helperfoos

def naiveApproach(messyStuff):
    pair = []
    #sort by x for the first time
    messyStuff.sort(key=lambda x: x[0])
    sortByX = messyStuff
    print(sortByX)

    return pair

def scanEntireArray(array):


def split(Array):
    if(len(Array)==1):
        return None
    elif(len(Array)==2):
        return array
    else:
        Array.sort(key=lambda x: x[1]) #sort by the second element
        closest0 = scanEntireArray(array)
        closest1 = min(split(array,mid/2),split(array+mid/2,mid/2))

        return closest0 if(closest0<closest1) else closest1




def main():
    points = helperfoos.grabArray()

    closest_pair=naiveApproach(points)







main()

import helperLibrary as helperfoos


def bruteForce(messyStuff):
    itemPair = []
    itemPair.append([messyStuff[0],messyStuff[1]])
    for index,item in enumerate(messyStuff):
        for OtherItem in messyStuff[index+1:]:
            if(helperfoos.dist_between_points(item,OtherItem)<
                helperfoos.dist_between_points(itemPair[0][0],itemPair[0][1])):
                itemPair=[]
                itemPair.append([item,OtherItem])
            elif(helperfoos.dist_between_points(item,OtherItem)==
                helperfoos.dist_between_points(itemPair[0][0],itemPair[0][1])):
                itemPair.append([item,OtherItem])

    return itemPair



def main():
    points = helperfoos.grabArray()
    results = bruteForce(points)
    print(results)







main()

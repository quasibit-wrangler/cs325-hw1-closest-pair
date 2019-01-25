

def split(Array, mid):
    array = sort_y(array)
    closest0 = scan(array)
    closest1 = min(split(array,mid/2),split(array+mid/2,mid/2))
    return (closest0<closest1) ? closest0 : closest1

    

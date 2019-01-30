import helperLibrary as h
import profiler as p
import time
import sys

@p.profile
def bruteForce(messyStuff):
    current_best = None
    for index,item in enumerate(messyStuff):
        for OtherItem in messyStuff[index+1:]:
            # looks at the items and creates a new array the new correct set.
            current_best = h.min_distance(current_best,[[item,OtherItem]])
    return current_best

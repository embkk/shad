import numpy as np


a = [1,2,3,3,3,3,3,3]



def most_frequent(arr):
    count = {}
    for x in arr:
        count[x] = count.get(x,0)+1
    max_key = max(count, key=count.get)
    return max_key

print(most_frequent(a))
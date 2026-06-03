
import numpy as np
n=int(input ("Enter no. of elements: "))
arr=np.zeros(n, dtype=int)
c=-1
for i in range(n):
    arr[i]=int(input("Enter elements: "))

if np.all(arr[:-1]<=arr[1:]): #np.all checks if all values are [true, true, true] and returns one single true/false
    print ("array is in ascending order")
else:
    print("Array is not in ascending order")
#time complexity: O(n), space = O(n)

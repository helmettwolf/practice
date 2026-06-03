import numpy as np 
def is_sorted(arr):
    return np.all(arr[:-1] <= arr[1:])
def check():

    n=int(input ("Enter the number of elements in array: "))
    arr=np.zeros(n, dtype=int)
    for i in range (n):
        arr[i]=int(input("Enter elements: "))
    for i in range (n-1):
        if arr[i]<=arr[i+1]:
            return True
        return False

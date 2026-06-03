import numpy as np
n=int(input ("Enter no. of elements: "))
arr=np.zeros(n, dtype=int)
c=-1
for i in range(n):
    arr[i]=int(input("Enter elements: "))
for i in range(n-1):
    if arr[i]<arr[i+1]:
        c=1
if c==1:
    print("Array is in ascending order.")
else:
    print ("Array is not in ascending order.")

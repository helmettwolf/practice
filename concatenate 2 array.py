import numpy as np
n=int(input ("Enter no. of elements: "))
n1=int(input("Enter no. of elements in second array: "))
arr1 = np.zeros(n, dtype=int)
arr2 = np.zeros(n1, dtype=int)
for i in range (n):
    arr1[i]=int(input("Enter your element in first array: "))
for j in range(n1):
    arr2[j]=int(input("Enter your element in second array: "))
arr3=np.concatenate((arr1, arr2))
print("Concatenated Array is: ", arr3)
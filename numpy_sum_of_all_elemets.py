import numpy as np

n = int(input("Enter no. of elements in your array: "))
arr = np.zeros(n, dtype=int)
for i in range(n):
    arr[i] = int(input("Enter the element: "))

print("Sum of all elements in the array:", np.sum(arr))

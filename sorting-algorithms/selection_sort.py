# Python program for implementation of Selection Sort

# Selection sort is fast then bubble sort because 
# In bubble sort, We have to write down on every iteration if condition is satisfy
# If we write down any thing in memory again and again then it take time
# but in selection sort we have to write down only one time end of first loop

A = [50,4,21,2,9,90,6]
n = len(A)

for i in range(n):
    min_key = i
    for j in range(i+1, n):
        if A[min_key] > A[j]:
            min_key = j
    A[i], A[min_key] = A[min_key], A[i]

print(A)
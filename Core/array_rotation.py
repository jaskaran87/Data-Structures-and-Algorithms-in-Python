# Python3 program to rotate an array by  
# d elements  
# Function to left rotate arr[] of size n by d*/ 
def leftRotate(arr, d, n):
    for i in range(d): 
        leftRotatebyOne(arr, n) 

# Function to left Rotate arr[] of size n by 1*/  
def leftRotatebyOne(arr, n): 
    last_element = arr[-1] 
    for i in range(0, n-1): 
        if i == 0:
            arr[-1] = arr[i+1] # [1,1,3,4,5,2]
            arr[i+1] = arr[i]
        else:
            lastelement = arr[-1]
            arr[-1] = arr[i+1]
            arr[i+1] = lastelement

    arr[0] = last_element

arr = [1, 2, 3, 4, 5, 6]

leftRotate(arr,2, len(arr)) 
print(arr)
arr = [12, 13, 1, 10, 34, 1] 
third = first = second = 0
for i in range(len(arr)): 
    if (arr[i] > first):
        third = second 
        second = first 
        first = arr[i] 
    elif (arr[i] > second): 
        third = second 
        second = arr[i]
    elif (arr[i] > third):
        third = arr[i]
print(first, second, third)

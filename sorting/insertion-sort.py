def insertion_Sort(arr):
    n = len(arr)
    for i in range (1, n):
        curr = arr[i]
        prev = i-1
        while prev>=0 and arr[prev] > curr:
            arr[prev+1] = arr[prev]
            prev -=1
        arr[prev+1] = curr
    return arr
    
arr1 = [4,1,5,2,3]
sorted_arr = insertion_Sort(arr1)
print(sorted_arr)
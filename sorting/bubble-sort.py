def bubble_Sort(arr):
    n = len(arr)
    for i in range (n-1):
        for j in  range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr1=[4,1,5,2,3]
sorted_arr=bubble_Sort(arr1)
print(sorted_arr)
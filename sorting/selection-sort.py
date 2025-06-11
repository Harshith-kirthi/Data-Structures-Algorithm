def selection_Sort(arr):
    n= len(arr)
    for i in range (n):
        min_index = i
        for j in range (i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr1=[1,5,3,8,9,2,4]
sorted_arr = selection_Sort(arr1)
print(sorted_arr)
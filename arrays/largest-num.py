#brute force approach
from typing import List
def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]
if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    print("The Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))

#recursive approach
def find_max(arr, n):
    max = arr[0]
    for i in range (0, n):
        if (max < arr[i]):
            max = arr[i]
    return max
if __name__ == "__main__":
    arr3 = [2, 5, 1, 3, 0]
    n = 5
    print(find_max(arr3, n))
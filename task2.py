def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0

    while low <= high:

        mid = (high + low) // 2
        count += 1
        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return (count, high)
    return -1


arr = [1.3, 3.4, 4.5, 10.1, 40.3]
x = 40.3
result = binary_search(arr, x)
if result != -1:
    print(result)
else:
    print("Element not found")

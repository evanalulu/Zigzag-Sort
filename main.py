#

arr = [5, 6, 3, 2, 1]

def zigzagSort(arr):
    arr.sort()
    start = 0
    end = len(arr) - 1
    sorted = []

    while (start < end):
        sorted.append(arr[end])
        sorted.append(arr[start])
        end -= 1
        start += 1

    if (start == end):
        sorted.append(arr[start])

    return sorted
        
print(zigzagSort(arr))

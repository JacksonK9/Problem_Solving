import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        target = arr[i]
        idx = 0
        for j in range(0, i):
            if target >= arr[j]:
                idx = j + 1
        if idx == i:
            pass
        else:
            arr.pop(i)
            arr.insert(idx, target)

def insertion_sort_db(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break


data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

ref_time = time.time()
insertion_sort(data)
print(data)
print(time.time() - ref_time)

data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

ref_time = time.time()
insertion_sort_db(data)
print(data)
print(time.time() - ref_time)

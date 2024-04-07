def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)

def partition(arr, left, right):
    pivot = left
    for i in range(left + 1, right + 1):
        if arr[i] <= arr[left]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]
    arr[pivot], arr[left] = arr[left], arr[pivot]
    return pivot




t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print(*arr)


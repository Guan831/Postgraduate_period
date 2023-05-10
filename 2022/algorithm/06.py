A = [12, 43, 7, 15, 9]
sortedA = sorted(A)


def binary_search(key, A):
    left = 0
    right = len(A) - 1
    while (right >= left):
        mid = left + (right - left) // 2
        if A[mid] == key:
            return mid
        elif A[mid] > key:
            right = mid - 1
        elif A[mid] < key:
            left = mid + 1

    return -1


result = []
for a in A:
    result.append(binary_search(a, sortedA))


print(result)

def find_rotation_count(A):
    n = len(A)
    if n == 0:
        return -1
    low = 0
    high = n - 1
    while low <= high:
        if A[low] <= A[high]:
            return low
        mid = (low + high) // 2
        next = (mid + 1) % n
        prev = (mid - 1 + n) % n
        if A[mid] <= A[next] and A[mid] <= A[prev]:
            return mid
        elif A[mid] <= A[high]:
            high = mid - 1
        elif A[mid] >= A[low]:
            low = mid + 1
    return -1

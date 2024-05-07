def get_median(arr1, arr2, n):
  arr = arr1 + arr2
  arr.sort()
  return (arr[n-1] + arr[n]) / 2

def check_greater(arr, number):
  for i in arr:
    if i >= number:
      return 'No, entered number is less than those in the array'
  return 'Yes, the entered number is greater than those in the array'

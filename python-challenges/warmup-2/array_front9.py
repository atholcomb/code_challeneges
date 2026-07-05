#!/usr/bin/python3
# written by: atholcomb
# array_front9.py

def array_front9(nums):
    if len(nums) > 4 and nums[-1] == 9:
        return False
    elif 9 in nums:
        return True
    else:
        return False

print(array_front9([1, 2, 9, 3, 4]))
print(array_front9([1, 2, 3, 4, 9]))
print(array_front9([1, 2, 3, 4, 5]))


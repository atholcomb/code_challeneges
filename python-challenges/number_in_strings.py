#!/usr/bin/python3
# written by: atholcomb
# number_in_strings.py

def numInStr(string_list):
    nums = '1234567890'
    result = set()
    
    for num in nums:
        for list_item in string_list:
            if num in list_item:
                result.add(list_item)
    
    return list(sorted(result))


print(numInStr(["1a", "a", "2b", "b"]))
print(numInStr(["abc", "abc10"]))
print(numInStr(["abc", "ab10c", "a10bc", "bcd"]))
print(numInStr(["this is a test", "test1"]))

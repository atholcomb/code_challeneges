#!/usr/bin/python3
# written by: atholcomb
# num_of_sublists.py
# Return the total number of lists inside a given list.

def num_of_sublists(some_list):
    count = 0 
    
    if not any(isinstance(i, list) for i in some_list):
        return 0
    else:
        for num in some_list:
            if num == list(num):
                count += 1

    return count


print(num_of_sublists([[1, 2, 3]])) # 1
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]])) # 2
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]])) # 4
print(num_of_sublists([1, 2, 3])) # 0

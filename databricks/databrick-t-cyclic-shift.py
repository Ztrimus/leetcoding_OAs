'''
File: databrick-t-cyclic-shift.py
Project: Coding
File Created: 26th Sep 2023 9:18 pm, Tuesday
Author: Saurabh Zinjad (GitHub: Ztrimus)
Email: zinjadsaurabh1997@gmail.com

Copyright (c) 2023 Saurabh Zinjad
'''

# array = [4,5,6,7,8,9,1,2,3]
# array = [1,2,3,4,5,6,7,8,9]
# array = [3,4,5,6,7,8,1,2]
array = [3,4,5,1,2]
# array = [3,2,1,5,4]
# array = [1,4,2,3]

def cyclic_check(array):
    result = -1
    array = array[::-1]
    len_array = len(array)
    
    for i in range(len_array):
        if len_array - array[i] == 0:
            result = (i+1)%len_array
        diff = abs(array[i] - array[i-1])
        if i != 0 and (diff not in [1, len_array-1]):
            result = -1

    return result

print(cyclic_check(array))
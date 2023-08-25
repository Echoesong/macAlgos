# First thought: write algo to determine when an hourglass occurs, then add those values together and stick them in an array. Add up the array at the end of the algorithm.

# Time complexity doesn't matter, always going to be O(1). Space complexity also maximum of O(1)? 

# Okay, so what is an hourglass? 
# 3 indices in a row, AND next array has 3 indices in a row below that (make left & rightmost 0), AND next array has 3 indices in a row.
# Okay, so I can just find all occurances of a 3x3, then make 2nd array elements 0 and 2 = 0.
# ^^Yeah pretty sure^^

# Iterate over the array, tracking indices; use an incrementer that stops when = 3
# When incrementer = 3, take the elements from the next 2 arrays that share the index values; for the 2nd one, make the 0th and 2nd element = 0.
# Add all elements, cache value somewhere.

# we know every hourglass starts at arr[0-3]
# arrays 4 & 5 don't have an hourglass
# Middle = if not array 4 or array 5 AND not index 4 or index 5

def hourglass(arr):
    storage = {}
    for i in range(16):
        storage[i] = 0
    incrementer = 0
    for i, array in enumerate(arr):
        if i == 4 or i == 5:
            continue
        for j in range(4):
            storage[incrementer] = (array[j] + array[j+1] + array[j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            incrementer += 1
    print(storage)
    maximum = 0
    for value in storage.values():
        if maximum <= value:
            maximum = value
    return maximum

arrz = [
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
]




print(hourglass(arrz))

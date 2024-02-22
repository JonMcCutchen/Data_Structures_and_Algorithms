# We are given two arrays. We have to find if these two arrays contain any matching elements.
# For example, array1 = ['a','b','c','x'] , array2 = ['x','y','z']
# This should return True as element 'x' appears in both arrays.

array1 = ['a','b','c','x']
array2 = ['x','y','z']

# Brute force approach
def brute_force_matching_elements(array1, array2):
    for i in array1:
        for j in array2:
            if i == j:
                return True
    return False

# Time complexity: O(n*m)

# Optimized approach
def optimized_matching_elements(array1, array2):
    dict = {}
    for i in range(len(array1)):
        dict[array1[i]] = True
    
    for i in range(len(array2)):
        if array2[i] in dict:
            return True
    
    return False


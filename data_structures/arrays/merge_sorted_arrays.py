#Given two sorted arrays, we need to merge them and create one big sorted array.
#For example, array1 = [1,3,5,7], array2 = [2,4,6,8]
#The result should be array = [1,2,3,4,5,6,7,8]

#One solution can be : we compare the corresponding elements of both arrays
#We add the smaller element to a new array and increment the index of the array from which the element was added.
#Again we compare the elements of both arrays and repeat the procedure until all the elements have been added.

def merge_sorted_arrays(array1, array2):
    merged_array = []
    i = 0
    j = 0
    flag = 0
    while i < len(array1) and j < len(array2): #The loop runs until we reach the end of either of the arrays
        if array1[i] <= array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1
        if i==len(array1):
            flag = 1

    if flag == 1:
        for k in range(j, len(array2)):
            merged_array.append(array2[k])
    else:
        for k in range(i, len(array1)):
            merged_array.append(array1[k])
    return merged_array

array1 = [1,3,5,7,9]
array2 = [2,4,6,8,10,11,12]
print(merge_sorted_arrays(array1, array2))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
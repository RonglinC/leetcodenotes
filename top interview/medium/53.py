import math
'''
time complexity is O(n^2)
space is O(1)
'''
def maximum_subarray_1(array):
    maxsubarray = -math.inf

    # i is the start index of the array
    for i in range(0,len(array)):
        current_array =0
        # j is the index that start with startindex until the len of array
        for j in range(i,len(array)):
            current_array+=array[j]# sum of the element
            maxsubarray=max(maxsubarray,current_array)
    return maxsubarray
            
def kadane(array):
    currentarray =array[0]
    maxsubarray=array[0]
    for i in range(2,len(array)):
        currentarray+=array[i]
        if currentarray<0:
            currentarray =0
        maxsubarray=max(maxsubarray,currentarray)
    return maxsubarray




if __name__ == '__main__':
    array =[-2,1,-3,4,-1,2,1,-5,4]
    print(maximum_subarray_1(array))
    print(kadane(array))
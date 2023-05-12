def longestConsecutive(nums):
     # store the length of each subsequence
     hash_dict = dict() 
    
    #keep track of the maximum subsequence length seen so far
     max_length = 0
     # check if number is already in the hash_dict
     for num in nums:
            #check if num-1 and num+1 are in hash_dict()
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)

                # if they present, add it them to current length of subsequence
                cur_length = 1 + left + right
                #update max_length
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length

     return max_length


if __name__ == '__main__':
     nums=[0,3,7,2,5,8,4,6,0,1]
     nums1=[100,4,200,1,3,2]
     print(longestConsecutive(nums))
     print(longestConsecutive(nums1))

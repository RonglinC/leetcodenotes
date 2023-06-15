def compress(chars)->int:
    n = len(chars)
    # i used for loop through array
    i =0
    #write the position
    write = 0
    while i <n:
        j =i
        #用j来找到从i开始相同的字符连续序列的长度
        while j <n and chars[j] == chars[i]:
            j+=1
        chars[write] = chars[i]
        write+=1
        if j-i >1:
            for c in str(j-1):
                chars[write]=c
                write+=1
        i=j
    # represent  the length of string
    return write
chars=["a","a","b","b","c","c","c"]
print(compress(chars))

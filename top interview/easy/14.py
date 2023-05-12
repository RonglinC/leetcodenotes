def longestCommonPrefix(self, strs):
    def lcp(start,end):
        if start == end:
            return strs[start]
        mid =(start+end)//2
        lcp_left,lcp_right =lcp(start,mid),lcp(mid+1,end)
        minLength=min(lcp_left,lcp_right)
        for i in range(0,minLength):
            if lcp_left[i] !=lcp_right[i]:
                return lcp_left[:i]
        return lcp_left[:minLength]
    return "" if not strs else lcp(0, len(strs) - 1)



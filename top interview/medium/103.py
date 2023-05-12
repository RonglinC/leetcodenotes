import collections
def zigzagLevelOrder(root):
    # if the node is empty
    if not root:
        return[]
    res =[]
    q = collections.deque() # initializze the double queue
    q.append(root) #压入队列
    # traversal all nodes
    while q:
        #题目返回的是按照层划分的数组
        res_temp =[]
        # length of q will change,bc we add thing into it 
        n = len(q)
        for i in range(n):
            temp=q.popleft()# pop the left element
            res_temp.append(temp.val)
            #如果当前节点在左边的数
            if temp.left:
                #put into queue as next level node to be traversal
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        # the result of each level
        res.append(res_temp)
        for j in range(len(res)):
            # reverse the even line, zigzag
            if j %2 ==1 :
                res[j].reverse()
        return res

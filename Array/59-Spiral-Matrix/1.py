# 之前不按照左闭又开的方式来进行传输数组会有问题 很长时间都在折腾index的问题！！！！

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        # represent the line number of matrix
        # 左臂又开就是后面多一个循环的对象 这样循环的守护也不会u想你换到哪里！！！！ 导致后面的循环条件种植再l<r
        left, right = 0, len(matrix[0])-1
        up, bottom = 0, len(matrix)-1
        # why use the boundary? 
        
        # 左闭右开为什么是等于呢？？？？？
        while left <= right and up <= bottom:
            
            # 如何表示第一行呢
            for lr in range(left, right):
                res.append(matrix[up][lr])
            
            for ub in range(up,bottom):
                res.append(matrix[ub][right])
           
            for rl in range(right, left, -1):
                res.append(matrix[bottom][rl])

            for bu in range(bottom, up, -1):
                res.append(matrix[bu][left])
                
            left +=1
            up +=1
            right-=1
            bottom -=1
            
        return res
                
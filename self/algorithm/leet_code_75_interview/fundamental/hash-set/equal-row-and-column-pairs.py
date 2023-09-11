class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
        如果行和列以相同的顺序包含相同的元素 即相等的数组，则认为二者是相等的
        """
        grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

        matrix_set = {}
        
        n = len(grid)
        for i in range(n):
            if tuple(grid[i]) not in matrix_set.keys():
                matrix_set[tuple(grid[i])] = 1
            else: matrix_set[tuple(grid[i])] +=1
        cnt = 0
        for i in range(n):
            print(tuple([_[i] for _ in grid]))
            if tuple([_[i] for _ in grid]) in matrix_set.keys():
                cnt += matrix_set[tuple([_[i] for _ in grid])]
        
        
        return cnt
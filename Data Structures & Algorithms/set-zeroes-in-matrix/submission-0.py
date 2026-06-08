class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = []
        c = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in r:
                    matrix[i][j] = 0
                if j in c:
                    matrix[i][j] = 0
        
        print(matrix)
